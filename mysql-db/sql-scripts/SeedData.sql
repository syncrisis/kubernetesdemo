SELECT * FROM sharks.Species;INSERT INTO `sharks`.`Species`
(`Id`,
`Name`,
`FriendlyName`)
VALUES
(1,
'Carcharodon carcharias',
'Great White');
INSERT INTO `sharks`.`Shark`
(`Id`,
`SpeciesId`,
`TagDate`,
`LatestPing`,
`Age`,
`Photo`,
`Length`,
`Name`,
`LastPingId`,
`ImageLink`)
VALUES
(1,
1,
null,
null,
19,
null,
20,
'Cait the Shark',
1,
'http://www.greatwhiteadventures.com/uploads/6/7/7/6/67762825/published/1114x860-gift-certificate.jpeg');
INSERT INTO `sharks`.`Shark`
(`Id`,
`SpeciesId`,
`TagDate`,
`LatestPing`,
`Age`,
`Photo`,
`Length`,
`Name`,
`LastPingId`,
`ImageLink`)
VALUES
(2,
1,
null,
null,
19,
null,
30,
'Nick the Shark',
2, 
'https://uc9d249b9b5d681e25c997d82d66.previews.dropboxusercontent.com/p/thumb/AAOwp-J9c12jJXOHLmhOfMXWeZ-fve3mzGjmLgpNpzh_NTsBtXHKHX8YjmaLdj69s4zJ2rwmlLqNnUmZYYoU9WCE59bbNpxmoz14GK5EBpHAYKVz9cf0ML0VEPa1jglWD_7mSo6OisRI7fjrk8uBVUbRGr0xzXYXOuiOI0CZQUinUoNPkrrk_GpDBFMylFAnUGIsuHFhsyHEt_TBoFCArFVC31tC4db3GUBBmCkvIpNJdw/p.jpeg?size=2048x1536&size_mode=3');
INSERT INTO `sharks`.`Ping`
(`Id`,
`Lat`,
`Lng`,
`SharkId`)
VALUES
(1,
41.481851,
-71.323026,
1);
INSERT INTO `sharks`.`Ping`
(`Id`,
`Lat`,
`Lng`,
`SharkId`)
VALUES
(2,
42.6895995,
-73.82030270000001,
2);
