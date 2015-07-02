CREATE DATABASE proximity;

CREATE TABLE `listing` (
  `id` int(30) NOT NULL AUTO_INCREMENT,
  `num_bedrooms` int(10) DEFAULT NULL,
  `num_bathrooms` int(10) DEFAULT NULL,
  `living_area` varchar(30) DEFAULT NULL,
  `lat` varchar(30) DEFAULT NULL,
  `lon` varchar(30) DEFAULT NULL,
  `exterior_stories` varchar(30) DEFAULT NULL,
  `pool` varchar(250) DEFAULT NULL,
  `dwelling_type` varchar(30) DEFAULT NULL,
  `list_date` date DEFAULT NULL,
  `list_price` decimal(8,2) DEFAULT NULL,
  `close_date` date DEFAULT NULL,
  `close_price` decimal(8,2) DEFAULT NULL,
  `zip` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8