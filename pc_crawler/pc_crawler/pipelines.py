import sqlite3
from scrapy.exceptions import DropItem
from jsonschema import validate, ValidationError


class PcCrawlerPipeline:
    def open_spider(self, spider):
        self.conn = sqlite3.connect('tech_scraper.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS computers
                              (processor TEXT, gpu TEXT, motherboard TEXT, ram TEXT)''')

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        schema = {
            "type": "object",
            "properties": {
                "processor": {"type": "string"},
                "gpu": {"type": "string"},
                "motherboard": {"type": "string"},
                "ram": {"type": "string"}
            },
            "required": ["processor", "gpu", "motherboard", "ram"]
        }
        try:
            validate(instance=item, schema=schema)
        except ValidationError as e:
            raise DropItem(f"Missing or invalid data: {e.message}")

        self.cursor.execute('''INSERT INTO computers (processor, gpu, motherboard, ram)
                               VALUES (?, ?, ?, ?)''',
                            (item['processor'], item['gpu'], item['motherboard'], item['ram']))
        self.conn.commit()
        return item
