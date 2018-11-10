import xml.etree.ElementTree as ET

def count_prices(root, level, prices):
    prices[root.attrib['color']] += level
    for child in root:
        prices = count_prices(child, level+1, prices)
    return prices

prices ={'red': 0, 'green': 0, 'blue': 0}

root = ET.fromstring(input())

print(*[prices[color] for color in count_prices(root, 1, prices)])
