CREATE TABLE `Species` (
  `Id` int(11) NOT NULL,
  `Name` varchar(250) DEFAULT NULL,
  `FriendlyName` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `Id_UNIQUE` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `Shark` (
  `Id` int(11) NOT NULL,
  `SpeciesId` int(11) NOT NULL,
  `TagDate` datetime DEFAULT NULL,
  `LatestPing` datetime DEFAULT NULL,
  `Age` int(11) DEFAULT NULL,
  `Photo` blob,
  `Length` decimal(10,0) DEFAULT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `LastPingId` int(11) DEFAULT NULL,
  `ImageLink` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `Id_UNIQUE` (`Id`),
  KEY `FK_Species_idx` (`SpeciesId`),
  CONSTRAINT `FK_Species` FOREIGN KEY (`SpeciesId`) REFERENCES `Species` (`Id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `Ping` (
  `Id` int(11) NOT NULL,
  `Lat` varchar(45) DEFAULT NULL,
  `Lng` varchar(45) DEFAULT NULL,
  `SharkId` int(11) DEFAULT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `Id_UNIQUE` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
SELECT * FROM sharks.Ping;