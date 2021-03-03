/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80023
 Source Host           : 127.0.0.1:3306
 Source Schema         : web_historien

 Target Server Type    : MySQL
 Target Server Version : 80023
 File Encoding         : 65001

 Date: 02/03/2021 17:52:48
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for Users
-- ----------------------------
DROP TABLE IF EXISTS `Users`;
CREATE TABLE `Users` (
  `u_id` int NOT NULL AUTO_INCREMENT,
  `u_mail` varchar(100) NOT NULL,
  `u_first_name` varchar(64) DEFAULT NULL,
  `u_last_name` varchar(64) DEFAULT NULL,
  `u_username` varchar(128) DEFAULT NULL,
  `u_password` varchar(32) DEFAULT NULL,
  `u_nation` varchar(64) DEFAULT NULL,
  `u_city` varchar(64) DEFAULT NULL,
  `u_address` varchar(500) DEFAULT NULL,
  `u_post_code` int DEFAULT NULL,
  PRIMARY KEY (`u_id`),
  UNIQUE KEY `u_mail` (`u_mail`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of Users
-- ----------------------------
BEGIN;
INSERT INTO `Users` VALUES (1, 'melody_cjy@163.com', 'CHU', 'Melody', 'Melody CHU', '123456', 'China', 'Shanghai', NULL, NULL);
INSERT INTO `Users` VALUES (2, 'amyshi2016@gmail.com', 'SHI', 'Yanjie', 'Yanjie SHI', '123456', 'France', 'Paris', NULL, NULL);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;


-- ----------------------------
-- Table structure for Museum
-- ----------------------------
DROP TABLE IF EXISTS `Museum`;
CREATE TABLE `Museum` (
  `m_id` int NOT NULL,
  `m_name` varchar(32) NOT NULL,
  `m_city` varchar(32) NOT NULL,
  `m_address` varchar(500) NOT NULL,
  `m_post_code` int DEFAULT NULL,
  `m_tel` int DEFAULT NULL,
  `m_mail` varchar(100) DEFAULT NULL,
  `m_document_limit` int DEFAULT NULL,
  `m_video_limit` int DEFAULT NULL,
  PRIMARY KEY (`m_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;


-- ----------------------------
-- Table structure for Archive
-- ----------------------------
DROP TABLE IF EXISTS `Archive`;
CREATE TABLE `Archive` (
  `a_code_reference` varchar(32) NOT NULL,
  `a_title` varchar(200) NOT NULL,
  `a_type` int NOT NULL,
  `a_author` varchar(100) NOT NULL,
  `a_description` varchar(2000) DEFAULT NULL,
  `a_museum_id` int NOT NULL,
  PRIMARY KEY (`a_code_reference`),
  KEY `Archive_a_museum_id_8c36ac4c_fk_Museum_m_id` (`a_museum_id`),
  CONSTRAINT `Archive_a_museum_id_8c36ac4c_fk_Museum_m_id` FOREIGN KEY (`a_museum_id`) REFERENCES `Museum` (`m_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;


-- ----------------------------
-- Table structure for Reservation
-- ----------------------------
DROP TABLE IF EXISTS `Reservation`;
CREATE TABLE `Reservation` (
  `r_id` int NOT NULL,
  `r_date_start` date NOT NULL,
  `r_date_end` date NOT NULL,
  `r_creator_id` int NOT NULL,
  `r_museum_id` int NOT NULL,
  PRIMARY KEY (`r_id`),
  KEY `Reservation_r_creator_id_034e70a3_fk_Users_u_id` (`r_creator_id`),
  KEY `Reservation_r_museum_id_b9057253_fk_Museum_m_id` (`r_museum_id`),
  CONSTRAINT `Reservation_r_creator_id_034e70a3_fk_Users_u_id` FOREIGN KEY (`r_creator_id`) REFERENCES `Users` (`u_id`),
  CONSTRAINT `Reservation_r_museum_id_b9057253_fk_Museum_m_id` FOREIGN KEY (`r_museum_id`) REFERENCES `Museum` (`m_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;


-- ----------------------------
-- Table structure for Res_Dem_Arch
-- ----------------------------
DROP TABLE IF EXISTS `Res_Dem_Arch`;
CREATE TABLE `Res_Dem_Arch` (
  `id` int NOT NULL AUTO_INCREMENT,
  `a_code_reference_id` varchar(32) NOT NULL,
  `r_id_id` int NOT NULL,
  `u_id_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Res_Dem_Arch_a_code_reference_id_658cf8bd_fk_Archive_a` (`a_code_reference_id`),
  KEY `Res_Dem_Arch_r_id_id_0a7547d8_fk_Reservation_r_id` (`r_id_id`),
  KEY `Res_Dem_Arch_u_id_id_1353b782_fk_Users_u_id` (`u_id_id`),
  CONSTRAINT `Res_Dem_Arch_a_code_reference_id_658cf8bd_fk_Archive_a` FOREIGN KEY (`a_code_reference_id`) REFERENCES `Archive` (`a_code_reference`),
  CONSTRAINT `Res_Dem_Arch_r_id_id_0a7547d8_fk_Reservation_r_id` FOREIGN KEY (`r_id_id`) REFERENCES `Reservation` (`r_id`),
  CONSTRAINT `Res_Dem_Arch_u_id_id_1353b782_fk_Users_u_id` FOREIGN KEY (`u_id_id`) REFERENCES `Users` (`u_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;

