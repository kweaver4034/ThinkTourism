-- phpMyAdmin SQL Dump
-- version 4.0.10deb1ubuntu0.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 15, 2020 at 09:28 AM
-- Server version: 5.5.62-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `keweave_tourism`
--

-- --------------------------------------------------------

--
-- Table structure for table `Choices`
--

CREATE TABLE IF NOT EXISTS `Choices` (
  `ChoiceID` int(11) NOT NULL AUTO_INCREMENT,
  `ChoiceText` varchar(20) NOT NULL,
  `ChoiceImageURL` varchar(300) NOT NULL,
  `QuestionID` int(11) NOT NULL,
  PRIMARY KEY (`ChoiceID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=47 ;

--
-- Dumping data for table `Choices`
--

INSERT INTO `Choices` (`ChoiceID`, `ChoiceText`, `ChoiceImageURL`, `QuestionID`) VALUES
(21, 'Hot', 'https://image.freepik.com/free-vector/fire-illustration_23-2147503409.jpg', 16),
(22, 'Cold', 'https://image.freepik.com/free-vector/white-paper-snowflake_1019-130.jpg', 16),
(23, 'Apple', 'https://image.freepik.com/free-vector/hand-drawn-apple-fruit-illustration_53876-2980.jpg', 17),
(24, 'Orange', 'https://img.freepik.com/free-vector/hand-drawn-colorful-orange-illustration_53876-2977.jpg?size=626&', 17),
(25, 'Coffee', 'https://img.freepik.com/free-vector/coffee-poster-with-realistic-white-porcelain-cup-textured-background_1284-10871.jpg?size=626&ext=jpg', 18),
(26, 'Tea', 'https://image.freepik.com/free-vector/realistic-white-cup-with-black-tea-mint_1284-2039.jpg', 18),
(29, 'Yes', '', 20),
(30, 'No', '', 20),
(31, 'Mango', 'https://img.freepik.com/free-vector/hand-drawn-mango-fruit-illustration_53876-2986.jpg?size=626&ext=jpg', 17),
(32, 'Apple Juice', 'https://image.freepik.com/free-vector/apple-juice-background_1212-608.jpg', 18),
(33, 'Orange Juice', 'https://image.freepik.com/free-vector/orange-juice_1268-39.jpg', 18),
(34, '1', '1', 21),
(35, '1', '1', 21),
(36, '1', '1', 22),
(37, '1', '1', 22),
(38, '1', '1', 23),
(39, '1', '1', 23),
(40, '1', '1', 23),
(41, '1', '1', 24),
(42, '1', '1', 24),
(43, '1', '1', 25),
(44, '1', '1', 25),
(45, '1', '1', 26),
(46, '1', '1', 26);

-- --------------------------------------------------------

--
-- Table structure for table `Log`
--

CREATE TABLE IF NOT EXISTS `Log` (
  `EntryID` int(11) NOT NULL AUTO_INCREMENT,
  `DateTime` datetime NOT NULL,
  `User` varchar(30) NOT NULL,
  `Action` varchar(30) NOT NULL,
  `Details` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`EntryID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

--
-- Dumping data for table `Log`
--

INSERT INTO `Log` (`EntryID`, `DateTime`, `User`, `Action`, `Details`) VALUES
(1, '2020-06-15 11:02:17', 'admin', 'CreatedGroup', 'Test SQL Log'),
(2, '2020-06-15 11:02:42', 'admin', 'CreatedQuestion', 'Test SQL Log'),
(3, '2020-06-15 11:04:21', 'admin', 'ViewedQuery', 'SELECT * FROM Questions'),
(4, '2020-06-15 11:05:27', 'admin', 'ViewedQuery', 'SELECT * FROM Questions'),
(5, '2020-06-15 11:07:44', 'admin', 'ViewedQuestionnaire', 'QuestionnaireTestGroup'),
(6, '2020-06-15 11:18:55', 'admin', 'ViewedQuery', 'SELECT * FROM Users'),
(7, '2020-06-15 11:19:20', 'admin', 'ViewedQuery', 'SELECT * FROM Users'),
(8, '2020-06-15 11:19:28', 'admin', 'ViewedQuery', 'SELECT * FROM Log'),
(9, '2020-06-15 11:21:35', 'admin', 'ViewedQuery', 'SELECT * FROM Users'),
(10, '2020-06-15 11:23:57', 'testhash', 'Logged In', '');

-- --------------------------------------------------------

--
-- Table structure for table `QuestionGroups`
--

CREATE TABLE IF NOT EXISTS `QuestionGroups` (
  `QuestionGroupID` int(11) NOT NULL AUTO_INCREMENT,
  `QuestionGroupName` varchar(40) NOT NULL,
  `DateCreated` date NOT NULL,
  PRIMARY KEY (`QuestionGroupID`),
  UNIQUE KEY `QuestionGroupName` (`QuestionGroupName`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=15 ;

--
-- Dumping data for table `QuestionGroups`
--

INSERT INTO `QuestionGroups` (`QuestionGroupID`, `QuestionGroupName`, `DateCreated`) VALUES
(6, 'QuestionnaireTestGroup', '2020-04-29'),
(7, 'Test Log Group', '2020-05-07'),
(9, 'Test Log Group 2', '2020-05-07'),
(10, 'Test Log Group 3', '2020-05-07'),
(11, 'Test Log Group 4', '2020-05-07'),
(12, 'TestSpaceGroup', '2020-05-14'),
(13, 'Test Space Group 2', '2020-05-15'),
(14, 'Test SQL Log', '2020-06-15');

-- --------------------------------------------------------

--
-- Table structure for table `Questions`
--

CREATE TABLE IF NOT EXISTS `Questions` (
  `QuestionID` int(11) NOT NULL AUTO_INCREMENT,
  `QuestionText` varchar(75) NOT NULL,
  `QuestionClass` varchar(20) NOT NULL,
  `QuestionType` varchar(20) NOT NULL,
  `QuestionGroupID` int(11) NOT NULL,
  PRIMARY KEY (`QuestionID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=27 ;

--
-- Dumping data for table `Questions`
--

INSERT INTO `Questions` (`QuestionID`, `QuestionText`, `QuestionClass`, `QuestionType`, `QuestionGroupID`) VALUES
(16, 'What temperature would you like your room?', 'Room', 'Text', 6),
(17, 'What fruit would you like with breakfast?', 'Food', 'Text', 6),
(18, 'What drink would you like with breakfast?', 'Food', 'Text', 6),
(20, 'Would you like a 6 am wake-up call?', 'Service', 'Text', 6),
(21, 'This is a test for the log', '1', '1', 1),
(22, 'This is a log test 2', '1', '1', 1),
(23, '1', '1', '1', 1),
(24, '1', '1', '1', 1),
(25, '1', '1', '1', 1),
(26, 'Test SQL Log', '1', '1', 1);

-- --------------------------------------------------------

--
-- Table structure for table `Respondents`
--

CREATE TABLE IF NOT EXISTS `Respondents` (
  `RespondentID` int(30) NOT NULL AUTO_INCREMENT,
  `RespondentName` varchar(50) NOT NULL,
  PRIMARY KEY (`RespondentID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `Respondents`
--

INSERT INTO `Respondents` (`RespondentID`, `RespondentName`) VALUES
(0, ''),
(1, 'kweaver'),
(2, 'testres'),
(3, 'testres2'),
(4, 'testres3'),
(5, 'testres4');

-- --------------------------------------------------------

--
-- Table structure for table `Responses`
--

CREATE TABLE IF NOT EXISTS `Responses` (
  `ResponseID` int(11) NOT NULL AUTO_INCREMENT,
  `RespondentID` int(11) DEFAULT NULL,
  `QuestionID` int(11) NOT NULL,
  `ChoiceID` int(11) NOT NULL,
  `DateTime` datetime NOT NULL,
  PRIMARY KEY (`ResponseID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=244 ;

--
-- Dumping data for table `Responses`
--

INSERT INTO `Responses` (`ResponseID`, `RespondentID`, `QuestionID`, `ChoiceID`, `DateTime`) VALUES
(1, 1, 16, 0, '2020-05-15 00:00:00'),
(2, 1, 16, 22, '2020-05-15 00:00:00'),
(3, 1, 17, 24, '2020-05-15 02:04:43'),
(4, 1, 18, 26, '2020-05-15 02:05:41'),
(5, 1, 17, 24, '2020-05-15 02:25:40'),
(6, 1, 16, 21, '2020-05-15 02:40:07'),
(7, 1, 17, 23, '2020-05-15 02:40:09'),
(8, 1, 18, 32, '2020-05-15 02:40:11'),
(9, 1, 16, 21, '2020-05-15 02:47:11'),
(10, 1, 17, 24, '2020-05-15 02:47:13'),
(11, 1, 18, 26, '2020-05-15 02:47:15'),
(12, 1, 20, 29, '2020-05-15 02:47:17'),
(13, 1, 16, 21, '2020-05-15 02:49:49'),
(14, 1, 17, 23, '2020-05-15 02:49:51'),
(15, 1, 18, 32, '2020-05-15 02:49:52'),
(16, 1, 20, 30, '2020-05-15 02:49:54'),
(17, 1, 20, 30, '2020-05-15 02:50:19'),
(18, 1, 16, 22, '2020-05-15 04:32:47'),
(19, 1, 16, 22, '2020-05-15 04:33:42'),
(20, 1, 16, 22, '2020-05-15 04:35:22'),
(21, 1, 16, 22, '2020-05-15 04:35:30'),
(22, 1, 16, 22, '2020-05-15 04:36:05'),
(23, 1, 16, 22, '2020-05-15 04:36:38'),
(24, 1, 16, 22, '2020-05-15 04:36:46'),
(25, 1, 16, 22, '2020-05-15 04:37:07'),
(26, 1, 16, 22, '2020-05-15 04:37:21'),
(27, 1, 16, 22, '2020-05-15 04:37:40'),
(28, 1, 16, 22, '2020-05-15 04:38:02'),
(29, 1, 16, 22, '2020-05-15 04:38:21'),
(30, 1, 16, 22, '2020-05-15 04:38:37'),
(31, 1, 16, 22, '2020-05-15 04:38:58'),
(32, 1, 16, 22, '2020-05-15 04:39:07'),
(33, 1, 16, 22, '2020-05-15 04:39:31'),
(34, 1, 16, 22, '2020-05-15 04:39:41'),
(35, 1, 16, 22, '2020-05-15 04:39:51'),
(36, 1, 16, 22, '2020-05-15 04:40:20'),
(37, 1, 16, 22, '2020-05-15 04:40:36'),
(38, 1, 16, 22, '2020-05-15 04:41:24'),
(39, 1, 16, 22, '2020-05-15 04:41:50'),
(40, 1, 16, 22, '2020-05-15 04:42:26'),
(41, 1, 16, 22, '2020-05-15 04:43:00'),
(42, 1, 16, 22, '2020-05-15 04:44:21'),
(43, 1, 16, 22, '2020-05-15 04:44:34'),
(44, 1, 16, 22, '2020-05-15 04:44:38'),
(45, 1, 16, 22, '2020-05-15 04:45:52'),
(46, 1, 16, 22, '2020-05-15 04:46:11'),
(47, 1, 16, 22, '2020-05-15 04:46:59'),
(48, 1, 16, 22, '2020-05-15 04:47:39'),
(49, 1, 16, 22, '2020-05-15 04:47:46'),
(50, 1, 16, 22, '2020-05-15 04:48:00'),
(51, 1, 16, 22, '2020-05-15 04:48:14'),
(52, 1, 16, 22, '2020-05-15 04:48:23'),
(53, 1, 16, 22, '2020-05-15 04:48:31'),
(54, 1, 16, 22, '2020-05-15 04:49:45'),
(55, 1, 16, 22, '2020-05-15 04:49:52'),
(56, 1, 16, 22, '2020-05-15 04:50:10'),
(57, 1, 16, 22, '2020-05-15 04:50:27'),
(58, 1, 16, 22, '2020-05-15 04:50:53'),
(59, 1, 16, 22, '2020-05-15 05:01:44'),
(60, 1, 16, 22, '2020-05-15 05:02:05'),
(61, 1, 16, 22, '2020-05-15 05:02:27'),
(62, 1, 16, 22, '2020-05-15 05:02:42'),
(63, 1, 16, 22, '2020-05-15 05:02:54'),
(64, 1, 16, 22, '2020-05-15 05:03:03'),
(65, 1, 16, 22, '2020-05-15 05:03:12'),
(66, 1, 16, 22, '2020-05-15 05:03:20'),
(67, 1, 16, 22, '2020-05-15 05:03:30'),
(68, 1, 16, 22, '2020-05-15 05:03:44'),
(69, 1, 16, 22, '2020-05-15 05:03:57'),
(70, 1, 16, 22, '2020-05-15 05:04:13'),
(71, 1, 16, 22, '2020-05-15 05:04:45'),
(72, 1, 16, 22, '2020-05-15 05:05:20'),
(73, 1, 16, 22, '2020-05-15 05:07:20'),
(74, 1, 16, 22, '2020-05-15 05:07:44'),
(75, 1, 16, 22, '2020-05-15 05:09:02'),
(76, 1, 16, 22, '2020-05-15 05:09:45'),
(77, 1, 16, 22, '2020-05-15 05:10:06'),
(78, 1, 16, 22, '2020-05-15 05:10:20'),
(79, 1, 16, 22, '2020-05-15 05:10:31'),
(80, 1, 16, 22, '2020-05-15 05:10:45'),
(81, 1, 16, 22, '2020-05-15 05:10:54'),
(82, 1, 16, 22, '2020-05-15 05:11:11'),
(83, 1, 16, 22, '2020-05-15 05:11:16'),
(84, 1, 16, 22, '2020-05-15 05:11:34'),
(85, 1, 16, 22, '2020-05-15 05:11:51'),
(86, 1, 16, 22, '2020-05-15 05:12:36'),
(87, 1, 16, 22, '2020-05-15 05:12:43'),
(88, 1, 16, 22, '2020-05-15 05:13:17'),
(89, 1, 16, 22, '2020-05-15 05:13:40'),
(90, 1, 16, 22, '2020-05-15 05:14:15'),
(91, 1, 16, 22, '2020-05-15 05:14:31'),
(92, 1, 16, 22, '2020-05-15 05:14:48'),
(93, 1, 16, 22, '2020-05-15 05:15:00'),
(94, 1, 16, 22, '2020-05-15 05:15:11'),
(95, 1, 16, 22, '2020-05-15 05:15:55'),
(96, 1, 16, 22, '2020-05-15 05:16:27'),
(97, 1, 16, 22, '2020-05-15 05:16:46'),
(98, 1, 16, 22, '2020-05-15 05:17:13'),
(99, 1, 16, 22, '2020-05-15 05:17:46'),
(100, 1, 16, 22, '2020-05-15 05:18:06'),
(101, 1, 16, 22, '2020-05-15 05:18:31'),
(102, 1, 16, 22, '2020-05-15 05:19:20'),
(103, 1, 16, 22, '2020-05-15 05:19:38'),
(104, 1, 16, 22, '2020-05-15 05:19:49'),
(105, 1, 16, 22, '2020-05-15 05:20:14'),
(106, 1, 16, 22, '2020-05-15 05:21:28'),
(107, 1, 16, 22, '2020-05-15 05:21:57'),
(108, 1, 16, 22, '2020-05-15 05:22:33'),
(109, 1, 16, 22, '2020-05-15 05:23:13'),
(110, 1, 16, 22, '2020-05-15 05:23:23'),
(111, 1, 16, 22, '2020-05-15 05:23:31'),
(112, 1, 16, 22, '2020-05-15 05:23:52'),
(113, 1, 16, 22, '2020-05-15 05:24:31'),
(114, 1, 16, 22, '2020-05-15 05:24:34'),
(115, 1, 16, 22, '2020-05-15 05:24:45'),
(116, 1, 16, 22, '2020-05-15 05:24:53'),
(117, 1, 16, 22, '2020-05-15 05:25:16'),
(118, 1, 16, 22, '2020-05-15 05:25:32'),
(119, 1, 16, 22, '2020-05-15 05:25:38'),
(120, 1, 16, 22, '2020-05-15 05:26:17'),
(121, 1, 16, 22, '2020-05-15 05:26:33'),
(122, 1, 16, 22, '2020-05-15 05:26:59'),
(123, 1, 16, 22, '2020-05-15 05:27:50'),
(124, 1, 16, 22, '2020-05-15 05:28:31'),
(125, 1, 16, 22, '2020-05-15 05:30:04'),
(126, 1, 16, 22, '2020-05-15 05:30:24'),
(127, 1, 16, 22, '2020-05-15 05:30:42'),
(128, 1, 16, 22, '2020-05-15 05:31:00'),
(129, 1, 16, 22, '2020-05-15 05:31:11'),
(130, 1, 16, 22, '2020-05-15 05:31:52'),
(131, 1, 16, 22, '2020-05-15 05:31:59'),
(132, 1, 16, 22, '2020-05-15 05:32:25'),
(133, 1, 16, 22, '2020-05-15 05:32:34'),
(134, 1, 16, 22, '2020-05-15 05:32:44'),
(135, 1, 16, 22, '2020-05-15 05:32:58'),
(136, 1, 16, 22, '2020-05-15 05:34:14'),
(137, 1, 16, 22, '2020-05-15 05:34:50'),
(138, 1, 16, 22, '2020-05-15 05:34:59'),
(139, 1, 16, 22, '2020-05-15 05:35:46'),
(140, 1, 16, 22, '2020-05-15 05:36:11'),
(141, 1, 16, 22, '2020-05-15 05:36:55'),
(142, 1, 16, 22, '2020-05-15 05:37:02'),
(143, 1, 16, 22, '2020-05-15 05:37:35'),
(144, 1, 16, 22, '2020-05-15 05:37:48'),
(145, 1, 16, 22, '2020-05-15 05:38:25'),
(146, 1, 16, 22, '2020-05-15 05:38:44'),
(147, 1, 16, 22, '2020-05-15 05:39:05'),
(148, 1, 16, 22, '2020-05-15 05:39:29'),
(149, 1, 16, 22, '2020-05-15 05:39:39'),
(150, 1, 16, 22, '2020-05-15 05:40:10'),
(151, 1, 16, 22, '2020-05-15 05:40:52'),
(152, 1, 16, 22, '2020-05-15 05:41:13'),
(153, 1, 16, 22, '2020-05-15 05:42:02'),
(154, 1, 16, 22, '2020-05-15 05:42:29'),
(155, 1, 16, 22, '2020-05-15 05:42:45'),
(156, 1, 16, 22, '2020-05-15 05:42:55'),
(157, 1, 16, 22, '2020-05-15 05:43:20'),
(158, 1, 16, 22, '2020-05-15 05:44:00'),
(159, 1, 16, 21, '2020-05-16 04:27:16'),
(160, 1, 17, 23, '2020-05-16 04:27:50'),
(161, 1, 18, 25, '2020-05-16 04:28:11'),
(162, 1, 20, 29, '2020-05-16 04:28:13'),
(163, 1, 16, 21, '2020-05-16 04:29:00'),
(164, 1, 17, 23, '2020-05-16 04:29:02'),
(165, 1, 17, 23, '2020-05-16 04:30:10'),
(166, 1, 18, 25, '2020-05-16 04:30:12'),
(167, 1, 18, 32, '2020-05-16 04:30:53'),
(168, 1, 18, 26, '2020-05-16 06:30:35'),
(169, 1, 20, 29, '2020-05-16 06:30:47'),
(170, 1, 18, 26, '2020-05-16 06:43:20'),
(171, 1, 20, 29, '2020-05-16 06:43:23'),
(172, 1, 18, 26, '2020-05-16 06:45:56'),
(173, 1, 20, 30, '2020-05-16 06:45:58'),
(174, 1, 20, 30, '2020-05-16 06:46:36'),
(175, 1, 16, 22, '2020-05-16 06:46:56'),
(176, 1, 17, 24, '2020-05-16 06:46:58'),
(177, 1, 18, 32, '2020-05-16 06:47:00'),
(178, 1, 20, 30, '2020-05-16 06:47:03'),
(179, 1, 20, 30, '2020-05-16 06:47:40'),
(180, 1, 20, 30, '2020-05-16 06:47:53'),
(181, 1, 16, 21, '2020-05-16 06:56:00'),
(182, 1, 16, 21, '2020-05-16 06:56:22'),
(183, 1, 16, 21, '2020-05-16 06:56:32'),
(184, 1, 16, 21, '2020-05-16 06:56:46'),
(185, 1, 17, 24, '2020-05-16 06:56:48'),
(186, 1, 17, 24, '2020-05-16 06:56:57'),
(187, 1, 18, 33, '2020-05-16 06:57:16'),
(188, 1, 18, 26, '2020-05-16 06:59:15'),
(189, 1, 16, 21, '2020-05-16 10:59:50'),
(190, 1, 17, 23, '2020-05-16 11:00:27'),
(191, 1, 18, 32, '2020-05-16 11:00:41'),
(192, 1, 20, 30, '2020-05-16 11:00:52'),
(193, 1, 17, 23, '2020-05-16 14:18:30'),
(194, 1, 16, 22, '2020-06-08 10:47:43'),
(195, 1, 16, 22, '2020-06-08 10:48:58'),
(196, 1, 17, 24, '2020-06-08 10:49:06'),
(197, 1, 18, 32, '2020-06-08 10:49:09'),
(198, 1, 20, 29, '2020-06-08 10:49:13'),
(199, 1, 16, 22, '2020-06-08 11:09:53'),
(200, 1, 17, 24, '2020-06-08 11:09:54'),
(201, 1, 18, 26, '2020-06-08 11:09:56'),
(202, 1, 20, 29, '2020-06-08 11:09:59'),
(203, 1, 16, 21, '2020-06-08 11:10:19'),
(204, 1, 17, 24, '2020-06-08 11:11:55'),
(205, 1, 18, 26, '2020-06-08 11:11:58'),
(206, 1, 20, 29, '2020-06-08 11:11:59'),
(207, 1, 20, 29, '2020-06-08 11:12:02'),
(208, 1, 16, 21, '2020-06-08 11:21:39'),
(209, 1, 17, 24, '2020-06-08 11:21:41'),
(210, 1, 18, 26, '2020-06-08 11:21:42'),
(211, 1, 20, 30, '2020-06-08 11:21:45'),
(212, 1, 16, 22, '2020-06-08 11:32:05'),
(213, 1, 17, 24, '2020-06-08 11:32:07'),
(214, 1, 18, 26, '2020-06-08 11:32:09'),
(215, 1, 20, 30, '2020-06-08 11:32:11'),
(216, 1, 16, 21, '2020-06-08 11:33:15'),
(217, 0, 16, 22, '2020-06-15 09:01:41'),
(218, 0, 17, 24, '2020-06-15 09:01:56'),
(219, 0, 18, 26, '2020-06-15 09:01:57'),
(220, 0, 20, 30, '2020-06-15 09:01:59'),
(221, 0, 16, 22, '2020-06-15 09:54:32'),
(222, 0, 17, 23, '2020-06-15 09:54:34'),
(223, 0, 18, 32, '2020-06-15 09:54:36'),
(224, 0, 20, 29, '2020-06-15 09:54:38'),
(225, 0, 16, 22, '2020-06-15 09:59:09'),
(226, 1, 16, 22, '2020-06-15 09:59:41'),
(227, 1, 17, 24, '2020-06-15 09:59:43'),
(228, 1, 18, 26, '2020-06-15 09:59:45'),
(229, 1, 20, 30, '2020-06-15 09:59:47'),
(230, 0, 16, 22, '2020-06-15 10:00:21'),
(231, 2, 17, 23, '2020-06-15 10:00:22'),
(232, 2, 18, 32, '2020-06-15 10:00:24'),
(233, 2, 20, 29, '2020-06-15 10:00:27'),
(234, 0, 16, 21, '2020-06-15 10:02:16'),
(235, 4, 16, 22, '2020-06-15 10:05:21'),
(236, 4, 17, 24, '2020-06-15 10:05:37'),
(237, 5, 16, 22, '2020-06-15 10:05:46'),
(238, 6, 16, 22, '2020-06-15 10:23:19'),
(239, 6, 17, 24, '2020-06-15 10:23:24'),
(240, 6, 16, 21, '2020-06-15 10:24:38'),
(241, 0, 17, 24, '2020-06-15 10:24:40'),
(242, 0, 18, 32, '2020-06-15 10:24:41'),
(243, 0, 20, 29, '2020-06-15 10:24:43');

-- --------------------------------------------------------

--
-- Table structure for table `Users`
--

CREATE TABLE IF NOT EXISTS `Users` (
  `UserID` int(11) NOT NULL AUTO_INCREMENT,
  `UserName` varchar(30) NOT NULL,
  `Password` varchar(50) NOT NULL,
  PRIMARY KEY (`UserID`),
  UNIQUE KEY `UserName` (`UserName`),
  UNIQUE KEY `UserID` (`UserID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `Users`
--

INSERT INTO `Users` (`UserID`, `UserName`, `Password`) VALUES
(1, 'admin', '745778706'),
(2, 'testhash', '1717222817');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
