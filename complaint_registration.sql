-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 20, 2022 at 01:02 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `complaint_registration`
--

-- --------------------------------------------------------

--
-- Table structure for table `admins`
--

CREATE TABLE `admins` (
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `pass` varchar(50) NOT NULL,
  `mode` varchar(36) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admins`
--

INSERT INTO `admins` (`name`, `email`, `gender`, `pass`, `mode`) VALUES
('pta', 'pta@gmail.com', 'male', '123', 'pta'),
('principal', 'principal@gmail.com', 'male', '123', 'principal');

-- --------------------------------------------------------

--
-- Table structure for table `complaint`
--

CREATE TABLE `complaint` (
  `Id` int(9) NOT NULL,
  `email` varchar(50) NOT NULL,
  `deaprtment` varchar(25) NOT NULL,
  `subject` varchar(200) NOT NULL,
  `description` varchar(2000) NOT NULL,
  `hod` varchar(10) NOT NULL,
  `principal` varchar(10) NOT NULL,
  `pta` varchar(10) NOT NULL,
  `status` varchar(50) NOT NULL,
  `solved` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `complaint`
--

INSERT INTO `complaint` (`Id`, `email`, `deaprtment`, `subject`, `description`, `hod`, `principal`, `pta`, `status`, `solved`) VALUES
(1, 'kd@gmail.com', 'COMPUTER', '0', 'sdfsfdsdfsd', 'false', 'false', 'true', 'pta rejected', 'rejected'),
(2, 'kd@gmail.com', 'CIVIL', '0', 'fgdsadfgdfbsdsffdfgdfg', 'true', 'false', 'false', 'hod solved', 'solved'),
(3, 'kd@gmail.com', 'COMPUTER', 'sdf', 'bnmbnmbnmbnmbn', 'true', 'false', 'false', 'Not viewed', ''),
(4, 'kd@gmail.com', 'COMPUTER', 'sdf', 'dfg', 'true', 'false', 'false', 'Not viewed', ''),
(5, 'kd@gmail.com', 'COMPUTER', 'kds', 'asdasd', 'true', 'false', 'false', 'Not viewed', ''),
(6, 'kd@gmail.com', 'COMPUTER', 'hgfn', 'vbnvbn', 'true', 'false', 'false', 'Not viewed', '');

-- --------------------------------------------------------

--
-- Table structure for table `hod`
--

CREATE TABLE `hod` (
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `pass` varchar(50) NOT NULL,
  `mode` varchar(10) NOT NULL,
  `department` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hod`
--

INSERT INTO `hod` (`name`, `email`, `gender`, `pass`, `mode`, `department`) VALUES
('hod2', 'hod2@gmail.com', 'male', '123', 'hod', 'CIVIL'),
('hod', 'hod@gmail.com', 'male', '123', 'hod', 'COMPUTER');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `email` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `gander` varchar(10) NOT NULL,
  `pass` varchar(50) NOT NULL,
  `User` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`email`, `name`, `gander`, `pass`, `User`) VALUES
('kd@gmail.com', 'kd', 'male', '123', 'user');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `complaint`
--
ALTER TABLE `complaint`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `hod`
--
ALTER TABLE `hod`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `complaint`
--
ALTER TABLE `complaint`
  MODIFY `Id` int(9) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
