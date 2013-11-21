# References

## CMB

http://www.slideshare.net/DataStax/cassandra-community-webinar-cmb-an-open-message-bus-for-the-cloud


## ES

http://asquera.de/opensource/2012/11/25/elasticsearch-pre-flight-checklist/
http://exploringelasticsearch.com/

## add to ansible

JAVA: http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/_linux.html


## Python drivers

http://pyelasticsearch.readthedocs.org/en/latest/


## SQS River

https://github.com/albogdano/elasticsearch-river-amazonsqs


## ES vs. Solr

http://blog.sematext.com/2012/08/23/solr-vs-elasticsearch-part-1-overview/




## boto -> CMB

  ```python
  from boto.sqs import regioninfo
  import logging 
  from boto.sqs.jsonmessage import JSONMessage
  
  logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
  
  cmbr = regioninfo.SQSRegionInfo(name='cmb', endpoint='192.168.21.253')
  cxn = cmbr.connect(aws_access_key_id='1XORFJ2OLF04TVR9SEZZ', aws_secret_access_key='vabqatbTzVDuJ1vPFBSLTmcsRFa+7RlJOd+tMVhp', port=6059, is_secure=False)
  q = cxn.create_queue('wat')
  msg = JSONMessage(body=dict(wat='hey'))
  assert q.write(msg)
  
  rmsg = q.read()
  print rmsg.get_body()
  ```
