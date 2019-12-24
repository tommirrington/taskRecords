CREATE DATABASE  IF NOT EXISTS `taskRecords` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */;
USE `taskRecords`;
-- MySQL dump 10.13  Distrib 8.0.15, for macos10.14 (x86_64)
--
-- Host: 127.0.0.1    Database: taskRecords
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tasks`
--

DROP TABLE IF EXISTS `tasks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tasks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user` varchar(255) DEFAULT NULL,
  `task_date` date DEFAULT NULL,
  `task_type` varchar(255) DEFAULT NULL,
  `reports_submitted` int(11) DEFAULT NULL,
  `tests_completed` int(11) DEFAULT NULL,
  `daily_report` varchar(1000) DEFAULT NULL,
  `notes` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tasks`
--

LOCK TABLES `tasks` WRITE;
/*!40000 ALTER TABLE `tasks` DISABLE KEYS */;
INSERT INTO `tasks` VALUES (48,'Stephanie','2019-11-06','Line',3,2,'All complete',''),(49,'Stephanie','2019-11-07','Stop',4,2,'All complete',''),(50,'Stephanie','2020-01-16','Other',4,0,'Need more time',''),(51,'Edmond','2019-12-04','Random',3,5,'Some issues found',''),(52,'Edmond','2019-11-07','Stop',1,1,'More time required','finished early'),(53,'Alex','2019-11-08','Other',3,4,'Complete',''),(54,'George','2019-11-06','Random',3,4,'Complete',''),(55,'George','2019-11-07','Random',3,4,'Complete',''),(56,'George','2019-11-08','Random',3,4,'Complete',''),(57,'Alex','2019-12-12','Random',3,4,'Additional task complete',''),(58,'Sally','2019-12-14','Stop',5,4,'Additional task complete',''),(59,'Sally','2019-12-14','Stop',5,7,'Additional task complete',''),(60,'Sally','2019-12-18','Stop',5,7,'Additional task complete',''),(61,'Sally','2019-12-19','Random',5,7,'Additional task complete',''),(62,'Other','2019-12-11','Random',3,2,'Two issues found','Tom assisted with tasks');
/*!40000 ALTER TABLE `tasks` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-24 16:48:01
