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
'Nick the Shark',
2, 
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
'Wes the Shark',
2, 
NULL);
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
39.71205,
-77.323026,
2);
