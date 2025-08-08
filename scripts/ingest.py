import pandas as pd
import xml.etree.ElementTree as ET

def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    records = []
    for person in root.findall(".//Table"):
        record = {}
        for elem in person:
            record[elem.tag] = elem.text
        records.append(record)
    return pd.DataFrame(records)

if __name__ == "__main__":
    df = parse_xml("data/Consolidated United Nations Security Council Sanctions List.xml")
    df.to_csv("output/raw_sanctions.csv", index=False)
    print("Saved raw CSV to output/raw_sanctions.csv")
