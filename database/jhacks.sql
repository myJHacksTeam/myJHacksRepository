-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 11, 2018 at 05:19 PM
-- Server version: 10.1.30-MariaDB
-- PHP Version: 7.2.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `jhacks`
--

-- --------------------------------------------------------

--
-- Table structure for table `Building`
--

CREATE TABLE `Building` (
  `tid` int(11) NOT NULL,
  `state` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL,
  `university` varchar(255) NOT NULL,
  `building` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `City`
--

CREATE TABLE `City` (
  `tid` int(11) NOT NULL,
  `state` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `State`
--

CREATE TABLE `State` (
  `tid` int(11) NOT NULL,
  `state` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Trashcan`
--

CREATE TABLE `Trashcan` (
  `id` int(11) NOT NULL,
  `nickname` varchar(255) DEFAULT NULL,
  `current_value` double DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `total_value` double DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `University`
--

CREATE TABLE `University` (
  `tid` int(11) NOT NULL,
  `state` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL,
  `university` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Building`
--
ALTER TABLE `Building`
  ADD PRIMARY KEY (`tid`,`state`,`city`,`university`,`building`);

--
-- Indexes for table `City`
--
ALTER TABLE `City`
  ADD PRIMARY KEY (`tid`,`state`,`city`);

--
-- Indexes for table `State`
--
ALTER TABLE `State`
  ADD KEY `tid` (`tid`);

--
-- Indexes for table `Trashcan`
--
ALTER TABLE `Trashcan`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nickname` (`nickname`);

--
-- Indexes for table `University`
--
ALTER TABLE `University`
  ADD PRIMARY KEY (`tid`,`state`,`city`,`university`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Trashcan`
--
ALTER TABLE `Trashcan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Building`
--
ALTER TABLE `Building`
  ADD CONSTRAINT `Building_ibfk_1` FOREIGN KEY (`tid`) REFERENCES `Trashcan` (`id`);

--
-- Constraints for table `City`
--
ALTER TABLE `City`
  ADD CONSTRAINT `City_ibfk_1` FOREIGN KEY (`tid`) REFERENCES `Trashcan` (`id`);

--
-- Constraints for table `State`
--
ALTER TABLE `State`
  ADD CONSTRAINT `State_ibfk_1` FOREIGN KEY (`tid`) REFERENCES `Trashcan` (`id`);

--
-- Constraints for table `University`
--
ALTER TABLE `University`
  ADD CONSTRAINT `University_ibfk_1` FOREIGN KEY (`tid`) REFERENCES `Trashcan` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
