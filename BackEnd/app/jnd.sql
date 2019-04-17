-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Apr 17, 2019 at 12:10 AM
-- Server version: 5.5.57-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.22

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `jnd`
--

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--

CREATE TABLE IF NOT EXISTS `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('23c704abf7da');

-- --------------------------------------------------------

--
-- Table structure for table `article`
--

CREATE TABLE IF NOT EXISTS `article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(600) DEFAULT NULL,
  `url` varchar(6000) DEFAULT NULL,
  `publicationdate` varchar(80) DEFAULT NULL,
  `content` varchar(12255) DEFAULT NULL,
  `domain_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `domain_id` (`domain_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `articlecategorie`
--

CREATE TABLE IF NOT EXISTS `articlecategorie` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `weight` varchar(250) DEFAULT NULL,
  `article_id` int(11) DEFAULT NULL,
  `categorie_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `article_id` (`article_id`),
  KEY `categorie_id` (`categorie_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `categorie`
--

CREATE TABLE IF NOT EXISTS `categorie` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(250) DEFAULT NULL,
  `desc` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `domain`
--

CREATE TABLE IF NOT EXISTS `domain` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domainname` varchar(600) DEFAULT NULL,
  `desc` varchar(800) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `domainname` (`domainname`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=53 ;

--
-- Dumping data for table `domain`
--

INSERT INTO `domain` (`id`, `domainname`, `desc`) VALUES
(1, 'https://www.trinidadexpress.com', 'The Trinidad and Tobago Express is one of three daily newspapers in Trinidad and Tobago. The Express is published by the Caribbean Communications Network and is headquartered on Independence Square in Port of Spain. The newspaper commenced operations on 6 June 1967.\n'),
(2, 'http://www.looptt.com', 'Loop is the number one source for Caribbean-wide local, regional and global content providing the best coverage of news, sports, entertainment, lifestyle, business, community and events. With our trusted team of journalists working locally in each market, we strive to bring you all the breaking and most up-to-date coverage of events, from a team you can trust.\r\nWith over 970,000 downloads to date, Loop currently provides content for 16 markets in the Caribbean, Central America and South Pacific.'),
(3, 'https://newsday.co.tt/', 'Trinidad and Tobago Newsday is a daily newspaper in Trinidad and Tobago. Newsday is the newest of the three daily papers after the Trinidad and Tobago Guardian and the Trinidad and Tobago Express respectively.'),
(4, 'https://www.guardian.co.tt', 'The Trinidad and Tobago Guardian is the longest running daily newspaper in the country, marking its centenary in 2017. The paper started life as the Trinidad Guardian in September 1917 by the newly formed Trinidad Publishing Company Limited.');

-- --------------------------------------------------------

--
-- Table structure for table `geotag`
--

CREATE TABLE IF NOT EXISTS `geotag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `locdesc` varchar(250) DEFAULT NULL,
  `location` varchar(250) DEFAULT NULL,
  `article_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `article_id` (`article_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `article`
--
ALTER TABLE `article`
  ADD CONSTRAINT `article_ibfk_1` FOREIGN KEY (`domain_id`) REFERENCES `domain` (`id`);

--
-- Constraints for table `articlecategorie`
--
ALTER TABLE `articlecategorie`
  ADD CONSTRAINT `articlecategorie_ibfk_1` FOREIGN KEY (`article_id`) REFERENCES `article` (`id`),
  ADD CONSTRAINT `articlecategorie_ibfk_2` FOREIGN KEY (`categorie_id`) REFERENCES `categorie` (`id`);

--
-- Constraints for table `geotag`
--
ALTER TABLE `geotag`
  ADD CONSTRAINT `geotag_ibfk_1` FOREIGN KEY (`article_id`) REFERENCES `article` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
