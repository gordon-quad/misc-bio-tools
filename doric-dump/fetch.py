#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
from StringIO import StringIO

url = 'http://tubic.tju.edu.cn/doric/info2.php?ac=ORI10010%03d'

def text_with_newlines(elem):
    text = ''
    for e in elem.recursiveChildGenerator():
        if isinstance(e, basestring):
            text += e.strip()
        elif e.name == 'br':
            text += '\n'
    return text

for i in range(237,238):
    try:
        resp = urllib2.urlopen(url % i)
        html = resp.read()
        doc = BeautifulSoup(html)
        result = {}
        result['AccId'] =    doc.body.div.findAll('div', recursive=False)[3].table.findAll('tr', recursive=False)[1].table.tr.findAll('td', recursive=False)[1].div.font.text.strip()
        result['Organism'] = doc.body.div.findAll('div', recursive=False)[3].table.findAll('tr', recursive=False)[1].td.table.findAll('tr', recursive=False)[1].findAll('td', recursive=False)[1].font.text.strip()
        result['RefSeq'] =   doc.body.div.findAll('div', recursive=False)[3].table.findAll('tr', recursive=False)[1].td.table.findAll('tr', recursive=False)[2].findAll('td', recursive=False)[1].font.text.strip()
        result['Topology'] = doc.body.div.findAll('div', recursive=False)[3].table.findAll('tr', recursive=False)[1].td.table.findAll('td', recursive=False)[1].font.text.strip()
        result['Lineage'] =  doc.body.div.findAll('div', recursive=False)[3].table.findAll('td', recursive=False)[1].font.text.strip()
        result['ChromSize']= doc.body.div.findAll('div', recursive=False)[3].table.findAll('td', recursive=False)[3].font.text.strip()
        result['ChromGC'] =  doc.body.div.findAll('div', recursive=False)[3].table.findAll('td', recursive=False)[5].font.text.strip()
        result['OriCLen'] =  doc.body.div.findAll('div', recursive=False)[3].table.findAll('tr', recursive=False)[2].findAll('td', recursive=False)[1].font.text.strip()
        result['OriCAT'] =   doc.body.div.findAll('div', recursive=False)[3].table.findAll('tr', recursive=False)[3].findAll('td', recursive=False)[1].font.text.strip()
        result['OriCIdx'] =  doc.body.div.findAll('div', recursive=False)[3].table.findAll('tr', recursive=False)[4].findAll('td', recursive=False)[1].div.font.text.strip()
        result['Cdc6Idx'] =  doc.body.div.findAll('div', recursive=False)[3].table.findAll('tr', recursive=False)[5].findAll('td', recursive=False)[1].font.text.strip()
        result['Extremes'] = doc.body.div.findAll('div', recursive=False)[3].table.findAll('tr', recursive=False)[6].findAll('td', recursive=False)[1].font.text.strip()
        result['Note'] =     doc.body.div.findAll('div', recursive=False)[3].table.findAll('tr', recursive=False)[7].findAll('td', recursive=False)[1].font.text.strip()
        result['Sequence'] = doc.body.div.findAll('div', recursive=False)[3].table.findAll('tr', recursive=False)[10].findAll('td', recursive=False)[1].pre.text.strip()
        result['Repeats'] =  text_with_newlines(doc.body.div.findAll('div', recursive=False)[3].table.findAll('tr', recursive=False)[11].findAll('td', recursive=False)[1].font.findAll('pre', recursive=False)[0]) + '\n' + \
                             text_with_newlines(doc.body.div.findAll('div', recursive=False)[3].table.findAll('tr', recursive=False)[11].findAll('td', recursive=False)[1].font.findAll('pre', recursive=False)[1])

        with open(result['AccId'] + '.rec', 'w') as f:
            for k in ['AccId', 'Organism', 'RefSeq', 'Topology', 'Lineage', 'ChromSize', 'ChromGC', 'OriCLen', 'OriCAT', 'OriCIdx', 'Cdc6Idx', 'Extremes', 'Note', 'Sequence', 'Repeats']:
                f.write(k + ': ' + result[k] + '\n')
    except e:
        print 'обосрались: ' + str(e)
