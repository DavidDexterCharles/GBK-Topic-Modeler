-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Apr 17, 2019 at 10:03 PM
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
  `TITLE` varchar(600) DEFAULT NULL,
  `SOURCE` varchar(600) DEFAULT NULL,
  `DATE` varchar(80) DEFAULT NULL,
  `CONTENT` varchar(12255) DEFAULT NULL,
  `domain_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `SOURCE` (`SOURCE`),
  KEY `domain_id` (`domain_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=35 ;

--
-- Dumping data for table `article`
--

INSERT INTO `article` (`id`, `TITLE`, `SOURCE`, `DATE`, `CONTENT`, `domain_id`) VALUES
(32, 'Small grants now available from Digicel Foundation ', 'http://www.looptt.com/content/small-grants-now-available-digicel-foundation', ' Created : 16 April 2019 ', 'The Digicel Foundation will host an open day for its ‘Extraordinary Projects Impacting Communities’ (EPIC)--a small grant initiative--on April 30 from 10AM to 3PM at the Digicel Hospitality Suite, Queen’s Park Oval in Port-of-Spain. According to a release issued by the Foundation, all registered community-based, faith-based and non-government organisations are invited to apply for an EPIC grant to implement impactful community projects in their communities. EPIC is an initiative that encourages registered organisations to propose small scale projects that enhance indoor or outdoor spaces that develop communities. Organisations that attend the open day will receive additional information and assistance with the application process for the grant which awards US$5,000 per projects to be completed within eight-week period. EPIC funding applications are also available online and can be found on their website. Completed forms can be submitted through email to digicelfoundationtt@digicelgroup.com or through postal mail to Digicel Foundation at the ANSA Centre, 11 C Maraval Road, St. Clair. The call for applications ends on April 30. Since the launch of EPIC in March 2016, the Digicel Foundation has invested TT$3 million in 39 community-based projects that have impacted over 20,000 persons in Trinidad and Tobago. The Foundation encourages EPIC applicants to collaborate with other public and private sector entities. Get the latest local and international news straight to your mobile phone for free: Copyright 2017 BY Trend Media | ALL RIGHTS RESERVED ', 2),
(33, ' Cuba to begin full internet access for mobile phones ', 'https://www.trinidadexpress.com/news/regional/cuba-to-begin-full-internet-access-for-mobile-phones/article_02d1718e-f89e-11e8-b5a3-77b7577f9faf.html', 'Dec 5, 2018 ', 'FILE - In this July 1, 2015 file photo, youths use a password protected wifi network coming from a five star hotel to surf the Internet on their smart phones in downtown Havana, Cuba. Cuba''s government announced on Tuesday, Dec. 4, 2018 that its citizens will be offered full internet access on mobile phones starting Thursday, Dec. 6, becoming one of the last nations to do so. (AP Photo/Desmond Boylan, File) FILE - In this July 1, 2015 file photo, youths use a password protected wifi network coming from a five star hotel to surf the Internet on their smart phones in downtown Havana, Cuba. Cuba''s government announced on Tuesday, Dec. 4, 2018 that its citizens will be offered full internet access on mobile phones starting Thursday, Dec. 6, becoming one of the last nations to do so. (AP Photo/Desmond Boylan, File) Cuba announced Tuesday night that its citizens will be offered full internet access for mobile phones beginning this week, becoming one of the last nations to offer such service. Mayra Arevich, president of the Cuban state telecom monopoly ETECSA, went on national television to say Cubans can begin contracting 3G service for the first time Thursday. Until now, Cubans have had access only to state-run email accounts on their phones. The Cuban government has been building a 3G network in cities across the island and some tourists, Cuban government officials and foreign businesspeople have had access to it for several years. The communist-governed island has one of the world''s lowest rates of internet use but that has been expanding rapidly since Presidents Barack Obama and Raul Castro declared detente in 2014. Expansion has not slowed with President Donald Trump''s partial rollback of relations. Cuba authorized home internet in 2017 and hundreds of public Wi-Fi connection points have opened in parks and plazas around the country. The new service will cost about 10 cents per megabyte, with packages ranging from 600 megabytes for about $7 to four gigabytes for about $30. Those prices are roughly in line with global standards but still out of reach for many Cubans who subsist on state salaries of about $30 a month. Cuba ran a fiber-optic connection to Venezuela in 2012, allowing the island to shift from slow and costly satellite links. It then began the slow process of allowing citizens to get online. The government opened state-run internet cafes in 2013, joined by Wi-Fi sites two years later. The number of sites has grown to more than 800. The Cuban internet is mostly uncensored but the government blocks a small number of sites like the U.S.-funded Radio and Television Marti networks and others that advocate for systematic change on the island. ETECSA vice president Tania Velázquez said the new service would come online in stages from Thursday through Saturday to avoid the congestion that struck the mobile network during a series of heavily criticized tests this year. DEATH came knocking at the door of Harish "Doll" Baldath, who was gunned down early Wednesday. KIDNAPPERS pretending to be police officers snatched a San Fernando businessman on Sunday an… AN EX-CONVICT who said financial woes led to him turning to the sale of marijuana, has been … INMATES are claiming that tuberculosis has been contracted by several of them at the Women’s… WAKES were held for two men who drowned at sea off Carli Bay, while vigils were being kept on the shore for two others still missing up to late yesterday. THE Coast Guard did its job properly as it searched the Carli Bay area on Sunday for the six distressed seamen, Agriculture Minister Clarence Rambharat said yesterday. Want to share good news story, or do you have information that should see the light of day? Then we want to hear from you. Instagram Please disable your ad blocker, whitelist our site, or purchase a subscription ', 1),
(34, 'Sat’s nasty attack on Tobagonians slammedNipsey Hussle’s Trini connection:Conspiracy theory in rapper’s deathDry season accelerates red palm miteCoconut estates under attackHotline coming to report sexual harassment on jobHarvesting the palms for Palm Sunday', 'https://www.guardian.co.tt/news/sats-nasty-attack-on-tobagonians-slammed-6.2.826298.62ee7f07ff', '20190416 ', 'Sanatan Dhar­ma Ma­ha Sab­ha sec­re­tary gen­er­al Sat Ma­haraj re­mained de­fi­ant yes­ter­day in the face of a furore over his con­tentious com­ments about the peo­ple of To­ba­go and a call from Mi­nor­i­ty Leader Wat­son Duke to apol­o­gise or face a hate cam­paign. “I have in­ten­tions to re­spond to Wat­son Duke and the crit­ics, I will re­ply at a time of my own choos­ing and the medi­um of my own choos­ing,” Ma­haraj said when con­tact­ed for com­ment hours af­ter Duke called for an apol­o­gy. Ma­haraj, how­ev­er, stood by his state­ment, say­ing it was the truth but said his re­sponse would come “af­ter the sea­son of good­will is over.” Ma­haraj drew the ire of many af­ter he at­tacked To­bag­o­ni­ans dur­ing on his TV Ja­gri­iti pro­gramme on Mon­day. “Noth­ing go­ing cor­rect in To­ba­go; they’re lazy. Six out of ten of them work­ing for the To­ba­go House of As­sem­bly, get­ting mon­ey from Port-of-Spain. They don’t want to work, and when they get a job, they go half past nine and 10 o’clock they go for break­fast,” Ma­haraj said dur­ing the pro­gramme. He al­so sug­gest­ed that oth­er able-bod­ied To­bag­o­ni­ans who were lazy pre­ferred to on­ly run crab and goat races and tar­get white women on beach­es whom they robbed and raped. A clip of Ma­haraj’s com­ments was soon shared on so­cial me­dia, prompt­ing an­gered re­spons­es on those plat­forms. Yes­ter­day, Duke called a press con­fer­ence at PSA head­quar­ters in Port-of-Spain where he con­demned Ma­haraj, say­ing the SDMS leader and his fol­low­ers should apol­o­gise or face a hate cam­paign from To­bag­o­ni­ans. “I wan­na tell Sat, any­time I know, any­time as Mi­nor­i­ty Leader in the To­ba­go House Of As­sem­bly, I know that you are in To­ba­go, we will give you a se­ri­ous un­wel­come and we will make your stay in To­ba­go hell,” Duke said. He added, “Some things you can leave silent, some things you have to lift your heel against. This is one. “He is look­ing for rel­e­vance in a coun­try that is far be­com­ing too large and too ed­u­cat­ed for his riffraff and his old chat. He has to find rel­e­vance by at­tack­ing any and every­one. Do the ho­n­ourable thing and apol­o­gise or you will face a hate cam­paign against you and against your or­gan­i­sa­tion.” Duke point­ed out that many To­bag­o­ni­ans work in Trinidad, par­tic­u­lar­ly those who had de­vel­oped skills which were not use­ful in the To­ba­go job mar­ket. In a Face­book post, Spir­i­tu­al Head of the Satya Anand Ashram, Pun­dit Satyanand Ma­haraj, slammed Ma­haraj’s com­ments as ob­scene and dis­gust­ing. He said the SDMS gen­er­al sec­re­tary had de­scribed the To­ba­go com­mu­ni­ty in the most dero­ga­to­ry terms and the In­di­an and Hin­du com­mu­ni­ty must be of­fend­ed and con­demn his state­ments. He added that if Hin­dus do not speak out and up against Ma­haraj, Hin­duism would be ad­verse­ly af­fect­ed, adding the Ma­ha Sab­ha sec­re­tary gen­er­al should al­so re­tire. Duke laud­ed Pun­dit Ma­haraj for his stance on the mat­ter and called for more in the Hin­du com­mu­ni­ty to fol­low suit. ', 4);

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
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `domain`
--

INSERT INTO `domain` (`id`, `domainname`, `desc`) VALUES
(1, 'https://www.trinidadexpress.com', 'The Trinidad and Tobago Express is one of three daily newspapers in Trinidad and Tobago. The Express is published by the Caribbean Communications Network and is headquartered on Independence Square in Port of Spain. The newspaper commenced operations on 6 June 1967.\n'),
(2, 'http://www.looptt.com', 'Loop is the number one source for Caribbean-wide local, regional and global content providing the best coverage of news, sports, entertainment, lifestyle, business, community and events. With our trusted team of journalists working locally in each market, we strive to bring you all the breaking and most up-to-date coverage of events, from a team you can trust.\r\nWith over 970,000 downloads to date, Loop currently provides content for 16 markets in the Caribbean, Central America and South Pacific.'),
(3, 'https://newsday.co.tt/', 'NOT SUPPORTED'),
(4, 'https://www.guardian.co.tt', 'The Trinidad and Tobago Guardian is the oldest daily newspaper in Trinidad and Tobago. Its first edition was published on Sunday 2nd September, 1917. The newspaper, now owned and published by Guardian Media Limited., began as a broadsheet but in November 2002 changed to tabloid format, known as the "G-sized Guardian');

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
