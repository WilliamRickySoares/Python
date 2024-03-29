from parsel import Selector
doc = """
<div>
    <ul>
        <li class="item-0"><a href="link1asdasdasdasd.html">first item</a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
"""
sel = Selector(text=doc)
a = sel.xpath('//li//@href').getall()
print(a)
b = sel.xpath(r'//li[re:test(@class, "item-\d$")]//@href').getall()
print(b)
