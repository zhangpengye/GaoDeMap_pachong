from xml.dom.minidom import parse
import xml.dom.minidom
DOMTree = xml.dom.minidom.parse('message.xml')
#获取xml文档对象
collection = DOMTree.documentElement   
TileCacheInfo = collection.getElementsByTagName('TileCacheInfo')[0]
rating = TileCacheInfo.getElementsByTagName('WKT')[0]
print(rating)
data = rating.childNodes[0].data
print(data)
#type = collection.getElementsByTagName('year')[1]
#print(type.childNodes[0].data)
#print(type)
#wkt = type.childNodes[0].data
#print(wkt)