## Notes

I written this very simple socks5 proxy server and client for understanding how protocol work.

```
docker-compose run --service-ports python
```

## reference

https://www.ietf.org/rfc/rfc1928.txt

According to the RFC 1928, the supported values of methods field defined as follows:

'00' NO AUTHENTICATION REQUIRED
'01' GSSAPI
'02' USERNAME/PASSWORD
'03' to X'7F' IANA ASSIGNED
'80' to X'FE' RESERVED FOR PRIVATE METHODS
'FF' NO ACCEPTABLE METHODS

https://docs.python.org/3/library/socket.html

https://docs.python.org/3/howto/sockets.html

https://docs.python.org/3/library/struct.html

https://rushter.com/blog/python-socks-server

http://socksipy.sourceforge.net

https://tools.ietf.org/html/draft-olteanu-intarea-socks-6-09

https://docs.axway.com/bundle/TransferCFT_35_UsersGuide_allOS_en_HTML5/page/Content/Prots/internet/use_Proxy_and_SOCKS_protocol.htm

https://medium.com/@nimit95/socks-5-a-proxy-protocol-b741d3bec66c

https://hpbn.co/transport-layer-security-tls
