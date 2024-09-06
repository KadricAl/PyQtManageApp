CREATE DATABASE  IF NOT EXISTS `btstest` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `btstest`;
-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: btstest
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `editors`
--

DROP TABLE IF EXISTS `editors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `editors` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `email` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `editors`
--

LOCK TABLES `editors` WRITE;
/*!40000 ALTER TABLE `editors` DISABLE KEYS */;
INSERT INTO `editors` VALUES (1,'a','a','a','a','a');
/*!40000 ALTER TABLE `editors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `uredjaji`
--

DROP TABLE IF EXISTS `uredjaji`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `uredjaji` (
  `id` int NOT NULL AUTO_INCREMENT,
  `datum` date NOT NULL,
  `ibfu` varchar(8) NOT NULL,
  `ibfm` varchar(8) DEFAULT NULL,
  `poslovna_j` varchar(45) DEFAULT NULL,
  `adresa` varchar(45) NOT NULL,
  `grad` varchar(20) NOT NULL,
  `telefon` varchar(15) DEFAULT NULL,
  `mail` varchar(45) DEFAULT NULL,
  `icc_id` varchar(20) DEFAULT NULL,
  `datum_zif` date DEFAULT NULL,
  `datum_zfm` date DEFAULT NULL,
  `id_broj` varchar(13) NOT NULL,
  `pdv_broj` varchar(12) DEFAULT NULL,
  `operater` varchar(20) NOT NULL,
  `korisnik` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `uredjaji`
--

LOCK TABLES `uredjaji` WRITE;
/*!40000 ALTER TABLE `uredjaji` DISABLE KEYS */;
INSERT INTO `uredjaji` VALUES (1,'2023-12-05','AA000010','AA000011','PJ','Adresa','Sarajevo','033100222','mail@mail.ba',NULL,'2022-05-05','2023-12-05','1234567891234','123456789123','BHT','Test'),(2,'2023-12-05','AB001020','AB001022','Nema','Test adresa','Sarajevo','061500600','test.mail.ba','11223344556677','2022-10-05','2023-12-05','1111111111111','111111111111','Telethings','User');
/*!40000 ALTER TABLE `uredjaji` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'btstest'
--

--
-- Dumping routines for database 'btstest'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-21 15:14:27
