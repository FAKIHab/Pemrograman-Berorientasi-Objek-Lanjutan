-- phpMyAdmin SQL Dump
-- version 5.2.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jul 14, 2026 at 08:10 PM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `universitas`
--

-- --------------------------------------------------------

--
-- Table structure for table `ambil`
--

CREATE TABLE `ambil` (
  `nim` char(10) NOT NULL,
  `kd_matkul` char(5) NOT NULL,
  `semester` enum('Gasal','Genap') NOT NULL,
  `thn_akademik` int NOT NULL,
  `presensi` int NOT NULL DEFAULT '0',
  `tugas` int NOT NULL DEFAULT '0',
  `uts` int NOT NULL DEFAULT '0',
  `uas` int NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `ambil`
--

INSERT INTO `ambil` (`nim`, `kd_matkul`, `semester`, `thn_akademik`, `presensi`, `tugas`, `uts`, `uas`) VALUES
('2422500021', 'MT101', 'Gasal', 2025, 100, 95, 80, 90);

-- --------------------------------------------------------

--
-- Table structure for table `dosen`
--

CREATE TABLE `dosen` (
  `nidn` varchar(16) NOT NULL,
  `gelar_depan` varchar(50) DEFAULT NULL,
  `nm_dosen` varchar(30) NOT NULL,
  `gelar_belakang` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `dosen`
--

INSERT INTO `dosen` (`nidn`, `gelar_depan`, `nm_dosen`, `gelar_belakang`) VALUES
('0102030405', 'Dr', 'Ibnu Setiaji', 'S.Si,M.Kom'),
('0201089201', 'DR', 'EZA PASTRO', 'M.Kom');

-- --------------------------------------------------------

--
-- Table structure for table `jadwal`
--

CREATE TABLE `jadwal` (
  `kd_jadwal` int NOT NULL,
  `semester` enum('Gasal','Genap') NOT NULL,
  `thn_akademik` int NOT NULL,
  `nidn` varchar(16) DEFAULT NULL,
  `kd_matkul` char(5) DEFAULT NULL,
  `kelompok` varchar(6) DEFAULT NULL,
  `hari` enum('Senin','Selasa','Rabu','Kamis','Jumat','Sabtu') DEFAULT NULL,
  `jam_mulai` time DEFAULT NULL,
  `jam_selesai` time DEFAULT NULL,
  `ruang` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `jadwal`
--

INSERT INTO `jadwal` (`kd_jadwal`, `semester`, `thn_akademik`, `nidn`, `kd_matkul`, `kelompok`, `hari`, `jam_mulai`, `jam_selesai`, `ruang`) VALUES
(17, 'Gasal', 2025, '0102030405', 'MT101', 'SI4A', 'Selasa', '08:00:00', '10:30:00', '1.3.2'),
(18, 'Gasal', 2025, '0102030405', 'MT101', 'SI1B', 'Kamis', '13:00:00', '15:30:00', '2.1.6'),
(19, 'Gasal', 2025, '0102030405', 'UM501', 'TI6J', 'Kamis', '16:30:00', '17:50:00', '2.1.3'),
(20, 'Genap', 2025, '0201089201', 'MT101', 'SI4J', 'Rabu', '16:30:00', '18:00:00', '2.1.6'),
(21, 'Gasal', 2025, '0201089201', 'UM501', 'SI4J', 'Kamis', '08:00:00', '10:30:00', '1.3.4');

-- --------------------------------------------------------

--
-- Table structure for table `mahasiswa`
--

CREATE TABLE `mahasiswa` (
  `nim` char(10) NOT NULL,
  `nm_mahasiswa` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `mahasiswa`
--

INSERT INTO `mahasiswa` (`nim`, `nm_mahasiswa`) VALUES
('2422500021', 'Fakih Arif Billah');

-- --------------------------------------------------------

--
-- Table structure for table `matkul`
--

CREATE TABLE `matkul` (
  `kd_matkul` char(5) NOT NULL,
  `nm_matkul` varchar(30) NOT NULL,
  `sks` enum('2','3','4') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `matkul`
--

INSERT INTO `matkul` (`kd_matkul`, `nm_matkul`, `sks`) VALUES
('MT101', 'Pengantar Teknologi Informasi', '4'),
('UM501', 'Etika Profesi', '3');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `ambil`
--
ALTER TABLE `ambil`
  ADD PRIMARY KEY (`nim`,`kd_matkul`),
  ADD KEY `fk_ambil_matkul` (`kd_matkul`);

--
-- Indexes for table `dosen`
--
ALTER TABLE `dosen`
  ADD PRIMARY KEY (`nidn`);

--
-- Indexes for table `jadwal`
--
ALTER TABLE `jadwal`
  ADD PRIMARY KEY (`kd_jadwal`),
  ADD KEY `fk_jadwal_nidn` (`nidn`),
  ADD KEY `fk_jadwal_matkul` (`kd_matkul`);

--
-- Indexes for table `mahasiswa`
--
ALTER TABLE `mahasiswa`
  ADD PRIMARY KEY (`nim`);

--
-- Indexes for table `matkul`
--
ALTER TABLE `matkul`
  ADD PRIMARY KEY (`kd_matkul`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `jadwal`
--
ALTER TABLE `jadwal`
  MODIFY `kd_jadwal` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `ambil`
--
ALTER TABLE `ambil`
  ADD CONSTRAINT `ambil_ibfk_1` FOREIGN KEY (`nim`) REFERENCES `mahasiswa` (`nim`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `ambil_ibfk_2` FOREIGN KEY (`kd_matkul`) REFERENCES `matkul` (`kd_matkul`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `jadwal`
--
ALTER TABLE `jadwal`
  ADD CONSTRAINT `fk_jadwal_dosen` FOREIGN KEY (`nidn`) REFERENCES `dosen` (`nidn`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_jadwal_matkul` FOREIGN KEY (`kd_matkul`) REFERENCES `matkul` (`kd_matkul`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
