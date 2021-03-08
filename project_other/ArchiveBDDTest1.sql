/*
 Navicat Premium Data Transfer

 Source Server         : LOCALHOST
 Source Server Type    : MySQL
 Source Server Version : 80023
 Source Host           : localhost:3306
 Source Schema         : Web_Historien

 Target Server Type    : MySQL
 Target Server Version : 80023
 File Encoding         : 65001

 Date: 06/03/2021 19:58:12
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for Users
-- ----------------------------
DROP TABLE IF EXISTS `Users`;
CREATE TABLE `Users`
(
    `u_ID`          int          NOT NULL AUTO_INCREMENT,
    `u_MailAddress` varchar(100) NOT NULL,
    `u_FirstName`   varchar(64)  DEFAULT NULL,
    `u_LastName`    varchar(64)  DEFAULT NULL,
    `u_UserName`    varchar(128) DEFAULT NULL,
    `u_PassWord`    varchar(32)  DEFAULT NULL,
    `u_Sex`         int          DEFAULT NULL,
    `u_Country`     varchar(64)  DEFAULT NULL,
    `u_City`        varchar(64)  DEFAULT NULL,
    `u_Address`     varchar(500) DEFAULT NULL,
    `u_ZipCode`     int          DEFAULT NULL,
    PRIMARY KEY (`u_ID`),
    UNIQUE KEY `u_MailAddress` (`u_MailAddress`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 11
  DEFAULT CHARSET = utf8;

-- ----------------------------
-- Records of Users
-- ----------------------------
BEGIN;
INSERT INTO `Users`
VALUES (1, 'melody_cjy@163.com', 'Melody', 'CHU', 'Melody CHU', '123456', 1, 'Chine', 'Shanghai', '16 rue Huanlong',
        200125);
INSERT INTO `Users`
VALUES (2, 'amyshi2016@gmail.com', 'Yanjie', 'SHI', 'Yanjie SHI', '123456', 1, 'France', 'Ivry-sur-Seine',
        '132 boulevard de Stalingrad', 94200);
INSERT INTO `Users`
VALUES (3, 'floergo@laposte.net', 'Floriane', 'OWXZAREK', 'Floriane OWXZAREK', '123456', 1, 'France', 'Paris',
        '90 rue de Tolbiac', 75013);
INSERT INTO `Users`
VALUES (4, 'cyril.lacheze@univ-paris1.fr', 'Cyril', 'LACHEZE', 'Cyril LACHEZE', '123456', 0, 'France', 'Paris',
        '90 rue de Tolbiac', 75013);
INSERT INTO `Users`
VALUES (5, 'exampleuser.01@gmail.com', 'Adam', 'BLACK', 'Adam BLACK', '123456', 1, 'France', 'Marseilles',
        '90 rue de Tolbiac', 75013);
INSERT INTO `Users`
VALUES (6, 'exampleuser.02@gamil.com', 'Corgi', 'WHITE', 'Corgi WHITE', '123456', 0, 'Allemagne', 'Berlin',
        '28 rue Akazienstraße', 10823);
INSERT INTO `Users`
VALUES (7, 'exampleuser.03@gmail.com', 'Jean', 'GREEN', 'Jean MICHEAL', '123456', 0, 'Belgique', 'Bruxelles',
        '4 Avenue Palmerston', 1000);
INSERT INTO `Users`
VALUES (8, 'exampleuser.04@gmail.com', 'Sarah', 'DE LA MARE', 'Sarah DE LA MARE', '123456', 1, 'États-Unis', 'Westmont',
        '921 Pasquinelli Dr', 60559);
INSERT INTO `Users`
VALUES (9, 'exampleuser.05@gmail.com', 'Annie', 'RAKAN', 'Annie RAKAN', '123456', 1, 'France', 'Paris',
        '90 rue de Tolbiac', 75013);
INSERT INTO `Users`
VALUES (10, 'exampleuser.06@gmail.com', 'Jack', 'JONES', 'Jack JONES', '123456', 0, 'Grèce', 'Larisa',
        '2 rue Papandreou', 41334);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;


/*
 Navicat Premium Data Transfer

 Source Server         : LOCALHOST
 Source Server Type    : MySQL
 Source Server Version : 80023
 Source Host           : localhost:3306
 Source Schema         : Web_Historien

 Target Server Type    : MySQL
 Target Server Version : 80023
 File Encoding         : 65001

 Date: 06/03/2021 19:57:43
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for Archive
-- ----------------------------
DROP TABLE IF EXISTS `Archive`;
CREATE TABLE `Archive`
(
    `a_ID`           varchar(32)  NOT NULL,
    `a_Folio`        int                                                      DEFAULT NULL,
    `a_Title`        varchar(200) NOT NULL,
    `a_Type`         int          NOT NULL,
    `a_Language`     varchar(16)  NOT NULL,
    `a_Author`       varchar(100) NOT NULL,
    `a_SaveLocation` int          NOT NULL,
    `a_Description`  varchar(2000) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
    PRIMARY KEY (`a_ID`),
    KEY `Archive_a_SaveLocation_8c36ac4c_fk_Museum_m_ID` (`a_SaveLocation`),
    CONSTRAINT `Archive_a_SaveLocation_8c36ac4c_fk_Museum_m_ID` FOREIGN KEY (`a_SaveLocation`) REFERENCES `Museum` (`m_ID`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

-- ----------------------------
-- Records of Archive
-- ----------------------------
BEGIN;
INSERT INTO `Archive`
VALUES ('10/EDT/204', 'Construction d\'une tuilerie : correspondance (1630)', 0, NULL, 'Français', 'Aniane',
        'La sous-série 5 S, l\'une des plus riches sur la thématique des commmunications, ne saurait laisser indifférents ceux qui s\'intéressent au développement économique du Languedoc au XIXe siècle. L\'Hérault a d\'ailleurs été l\'un des premiers départements français à posséder une ligne de chemin de fer. La ligne de Montpellier à Sète, projetée dès 1834, entreprise en 1837, était en service en 1839. Les dossiers d\'enquête, préalables à la mise en oeuvre des voies ferrées, recèlent de nombreux renseignements d\'ordre économique, notamment sur la production viticole et minière, le commerce et le roulage sur les routes destinées à être doublées par le chemin de fer. Les premiers tronçons ont été conçus dans un intérêt purement local, d\'où des études sur le trafic routier et la rentabilité des lignes. Ils contiennent aussi des délibérations, pétitions, interventions, etc., relatives au choix du tracé des lignes. On y trouve en outre de nombreux renseignements sur l\'urbanisme des grandes villes, sur le choix de l\'emplacement des gares de Montpellier (5 S 72-76, 615-621), sur l\'agrandissement du port de Sète (5 S 63, 126-130, 164-168), sur les déraillements, les pannes et les accidents qui arrivent fréquemment au cours des premières années d\'exploitation ; sur les inévitables procès entraînés par tous les grands travaux publics. Le contentieux de l\'intérêt local compte à lui seul plus de 18 gros dossiers (5 S 427-440, 1386-1389). Mentionnons, pour finir, l\'abondante documentation sur le matériel ferroviaire, dans les réseaux d\'intérêt général ou local et dans les tramways.',
        1);
INSERT INTO `Archive`
VALUES ('105/FI/1337',
        'Une des photographies composant le fonds Lunais-Bruère : le centre-ville de Blois après les destructions de la seconde guerre mondiale. Négatif stéréoscopique',
        2, NULL, 'Français', 'Fr',
        'Les documents donnés par cette famille blésoise illustrent parfaitement les soubresauts de la première moitié du XXe siècle : journaux intimes d’un abbé sous l’Occupation, lettres adressés à ses parents par un jeune homme effectuant son service du travail obligatoire (STO), papiers concernant la participation à des jeunesses catholiques féminines, etc. Accompagné d’une collection très riche de photographies et de plaques de verres, ce fonds permet de se plonger au cœur d’une famille : au-delà de l’aspect patrimonial, il s’agit d’une source précieuse pour étudier la vie quotidienne et les relations sociales sur une période de plus de 60 ans.',
        7);
INSERT INTO `Archive`
VALUES ('122/J/1273',
        'Projet de création d\'un \"centre de congrès et de rencontres\" en lieu et place de la Halle aux grains à Blois (carnet de croquis, 1975-1976)',
        2, 129, 'Français', 'Fr',
        'Les dossiers de travaux et les plans de ce cabinet d’architecture constituent un ensemble unique à l’échelle du Blésois. Couvrant toute la seconde moitié du XXe siècle, il renferme certains grands projets architecturaux ou urbanistiques (le projet abandonné de construction d’une salle de spectacle à la place de la Halle aux Grains de Blois par exemple). Le fonds offre également une large panoplie de chantiers de moindre envergure mais non moins significatifs (en particulier les travaux de rénovation du vieux Blois, auxquels MM. Aubry et Ferrieux participèrent activement).',
        3);
INSERT INTO `Archive`
VALUES ('19770932/1', 'Service des chemins de fer - Sous-direction des transports ferroviaires (1938-1960)', 0, NULL,
        'Français', 'Sous-direction des transports ferroviaires',
        'Les dossiers portant les numéros TT 27L à TT 282, concernent l\'électrification des chemins de fer entre 1938 et 1960. Il s\'agit de dossiers, probablement incomplets, retrouvés dans le local de la mission des Archives Nationales du Ministère des Travaux Publics.\n\nIl n\'a pas été possible à la mission de réunir une documentation sur l\'historique de l\'électrification des chemins de fer. Une étude devra être faite au moment du triage de l\'ensemble des archives du service des chemins de fer dont une grande partie est conservée sans inventaire dans une cave du 246 boulevard Saint-Germain',
        2);
INSERT INTO `Archive`
VALUES ('30/FI/1/34', 'Le château de La Ferté-Imbault : aquarelle de Louis de La Saussaye, 8 août 1832', 1, NULL,
        'Français', 'Château de La Ferté-Imbault',
        'Cet ensemble de documents, couvrant la période 1341-1891, est un bon exemple de ce que sont les archives des familles aristocratiques. En plus des papiers de gestion du domaine (baux, acquêts, fois et hommages, pièces de procédures judiciaires…), on y trouve nombre de pièces relatives à des branches plus ou moins éloignées de la famille (en particulier la famille d’Estampes). Le travail d’indexation par l’archiviste est ici essentiel pour que la recherche s’effectue à la fois par personne et par localité.',
        3);
INSERT INTO `Archive`
VALUES ('MC/ET/I/64',
        'Marché de Sasbout de Varicq, gentilhomme hollandais, demeurant à la Tuilerie du Pré-aux-Clercs, 9 février 1608',
        0, NULL, 'Français', 'Germain TRONSON',
        '1608 : janvier à avril, juin, août, octobre et décembre. 1608, 24 avril : copie . Sur la couverture, note de Germain Tronson indiquant qu\'en raison de son association avec Germain Desmarquets (ET/LVIII) au commencement d\'avril, les autres mois sont dans la pratique de celui-ci.',
        2);
INSERT INTO `Archive`
VALUES ('MC/ET/XXXIII/23',
        'Minutes et répertoires du notaire Yves BOURGEOIS, 20 septembre 1539 - 26 août 1549 (étude XXXIII)', 0, 492,
        'Français', 'Yves BOURGEOIS',
        'Minutes et répertoires : la loi 2008-696 du 15 juillet 2008 relative aux archives a fixé à 75 ans à compter de la date de l\'acte, ou à 25 ans à compter de la date du décès de l\'intéressé si ce délai est plus bref, le délai de communication des minutes et répertoires des notaires ; ce délai est porté à 100 ans à compter de la date de l\'acte si le document se rapporte à un mineur (code du Patrimoine, articles L213-2, 4e d et 5e).\n\n',
        5);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;


/*
 Navicat Premium Data Transfer

 Source Server         : LOCALHOST
 Source Server Type    : MySQL
 Source Server Version : 80023
 Source Host           : localhost:3306
 Source Schema         : Web_Historien

 Target Server Type    : MySQL
 Target Server Version : 80023
 File Encoding         : 65001

 Date: 06/03/2021 19:57:53
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for Museum
-- ----------------------------
DROP TABLE IF EXISTS `Museum`;
CREATE TABLE `Museum`
(
    `m_ID`              int                                                     NOT NULL,
    `m_Name`            varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    `m_City`            varchar(32)                                             NOT NULL,
    `m_Address`         varchar(500)                                            NOT NULL,
    `m_ZipCode`         int          DEFAULT NULL,
    `m_Tel`             varchar(20)  DEFAULT NULL,
    `m_Mail`            varchar(100) DEFAULT NULL,
    `m_NbDocumentLimit` int          DEFAULT NULL,
    `m_NbVideoLimit`    int          DEFAULT NULL,
    PRIMARY KEY (`m_ID`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

-- ----------------------------
-- Records of Museum
-- ----------------------------
BEGIN;
INSERT INTO `Museum`
VALUES (1, 'Domaine Départemental Pierresvives', 'Montpellier', '907 rue Profesurur Blayac', 34080,
        '(+33) 4 67 67 30 00', ' pierresvives@herault.fr', 17, 17);
INSERT INTO `Museum`
VALUES (2, 'Archives nationales - Site de Pierrefitte-sur-Seine', 'Pierrefitte-sur-Seine', '59 rue Guynemer', 93380,
        '(+33) 1 75 47 20 02', 'archives-nationales@culture.gouv.fr', 12, 12);
INSERT INTO `Museum`
VALUES (3, 'Service des archives - Bureau Régional de Bourgogne-Franche-Comté', 'Besançon',
        '8 Avenue Denfert Rochereau', 25000, '(+33) 3 81 61 61 46', 'odile.boyer@bourgognefranchecomte.fr', 15, 15);
INSERT INTO `Museum`
VALUES (4, 'Service des archives - Bureau Ardeche', 'Privas', 'Place André-Malraux', 7000, '(+33) 4 75 66 98 00',
        'archives@ardeche.fr', 15, 15);
INSERT INTO `Museum`
VALUES (5, 'Service des archives - Bureau Gard', 'Nîmes', '365 rue du Forez', 30000, '(+33) 4 66 05 05 10',
        'archives@gard.fr', 10, 10);
INSERT INTO `Museum`
VALUES (6, 'Service des archives - Bureau Marne', 'Reims', '44 avenue de l\'Yser', 51100, '(+33) 3 26 68 06 69',
        'archives51@marne.fr', 12, 12);
INSERT INTO `Museum`
VALUES (7, 'Service des archives - Bureau Pas-de-Calais', 'Arras', '12 place de la Préfecture', 62000,
        '(+33) 3 21 71 10 90', 'archives62@pasdecalais.fr', 11, 11);
INSERT INTO `Museum`
VALUES (8, 'Service des archives - Bureau Yonne', 'Auxerre', '5 rue Jean-Moulin', 89000, '(+33) 3 86 94 89 00',
        'archives@yonne.fr', 15, 15);
INSERT INTO `Museum`
VALUES (9, 'Service des archives - Bureau Puy-de-Dôme', 'Clermont-Ferrand', '75 rue de Neyrat', 63100,
        '(+33) 4 73 23 45 80', 'archives@puy-de-dome.fr', 14, 14);
INSERT INTO `Museum`
VALUES (10, 'Service des archives - Bureau Pays de la loire', 'Nantes Cedex 9', '1 rue de la Loire', 44966,
        '(+33) 2 28 20 52 48', 'agnes.dejob@paysdelaloire.fr', 17, 17);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;


/*
 Navicat Premium Data Transfer

 Source Server         : LOCALHOST
 Source Server Type    : MySQL
 Source Server Version : 80023
 Source Host           : localhost:3306
 Source Schema         : Web_Historien

 Target Server Type    : MySQL
 Target Server Version : 80023
 File Encoding         : 65001

 Date: 06/03/2021 19:58:06
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for Reservation
-- ----------------------------
DROP TABLE IF EXISTS `Reservation`;
CREATE TABLE `Reservation`
(
    `r_ID`                  int  NOT NULL,
    `r_EndDate`             date NOT NULL COMMENT 'Finis avant JJ/MM/AAAA',
    `r_Status`              int  NOT NULL COMMENT '0 = Pas encore aller; 1 = suis allé',
    `r_MuseumID`            int  NOT NULL,
    `r_ProviderID`          int  NOT NULL,
    `r_ProviderHasSent`     int  NOT NULL COMMENT '0 = Pas encore envoyer; 1 = est envoyé',
    `r_DemanderHasReceived` int  NOT NULL COMMENT '0 = Pas encore recevoir; 1 = est reçu',
    PRIMARY KEY (`r_ID`),
    KEY `Reservation_r_ProviderID_034e70a3_fk_Users_u_ID` (`r_ProviderID`),
    KEY `Reservation_r_MuseumID_b9057253_fk_Museum_m_ID` (`r_MuseumID`),
    CONSTRAINT `Reservation_r_MuseumID_b9057253_fk_Museum_m_ID` FOREIGN KEY (`r_MuseumID`) REFERENCES `Museum` (`m_ID`),
    CONSTRAINT `Reservation_r_ProviderID_034e70a3_fk_Users_u_ID` FOREIGN KEY (`r_ProviderID`) REFERENCES `Users` (`u_ID`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

-- ----------------------------
-- Records of Reservation
-- ----------------------------
BEGIN;
INSERT INTO `Reservation`
VALUES (1, '2021-03-01', 1, 1, 1, 2, 4);
INSERT INTO `Reservation`
VALUES (2, '2021-03-04', 1, 1, 0, 6, 7);
INSERT INTO `Reservation`
VALUES (3, '2021-03-19', 0, 0, 0, 3, 2);
INSERT INTO `Reservation`
VALUES (4, '2021-03-20', 0, 0, 0, 2, 2);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;


/*
 Navicat Premium Data Transfer

 Source Server         : LOCALHOST
 Source Server Type    : MySQL
 Source Server Version : 80023
 Source Host           : localhost:3306
 Source Schema         : Web_Historien

 Target Server Type    : MySQL
 Target Server Version : 80023
 File Encoding         : 65001

 Date: 06/03/2021 19:57:59
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for Res_Dem_Arch
-- ----------------------------
DROP TABLE IF EXISTS `Res_Dem_Arch`;
CREATE TABLE `Res_Dem_Arch`
(
    `rad_ID`            int         NOT NULL AUTO_INCREMENT,
    `rad_ArchiveID`     varchar(32) NOT NULL,
    `rad_ReservationID` int         NOT NULL,
    `rad_UsersID`       int         NOT NULL,
    PRIMARY KEY (`rad_ID`),
    KEY `Res_Dem_Arch_rad_ArchiveID_658cf8bd_fk_Archive_a` (`rad_ArchiveID`),
    KEY `Res_Dem_Arch_rad_ReservationID_0a7547d8_fk_Reservation_r_id` (`rad_ReservationID`),
    KEY `Res_Dem_Arch_rad_UsersID_1353b782_fk_Users_u_id` (`rad_UsersID`),
    CONSTRAINT `Res_Dem_Arch_rad_ArchiveID_658cf8bd_fk_Archive_a_ID` FOREIGN KEY (`rad_ArchiveID`) REFERENCES `Archive` (`a_ID`),
    CONSTRAINT `Res_Dem_Arch_rad_ReservationID_0a7547d8_fk_Reservation_r_ID` FOREIGN KEY (`rad_ReservationID`) REFERENCES `Reservation` (`r_ID`),
    CONSTRAINT `Res_Dem_Arch_rad_UsersID_1353b782_fk_Users_u_ID` FOREIGN KEY (`rad_UsersID`) REFERENCES `Users` (`u_ID`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 7
  DEFAULT CHARSET = utf8;

-- ----------------------------
-- Records of Res_Dem_Arch
-- ----------------------------
BEGIN;
INSERT INTO `Res_Dem_Arch`
VALUES (1, '10/EDT/204', 1, 1);
INSERT INTO `Res_Dem_Arch`
VALUES (2, '10/EDT/204', 3, 7);
INSERT INTO `Res_Dem_Arch`
VALUES (3, '122/J/1273', 3, 4);
INSERT INTO `Res_Dem_Arch`
VALUES (4, '122/J/1273', 2, 6);
INSERT INTO `Res_Dem_Arch`
VALUES (5, '105/FI/1337', 3, 5);
INSERT INTO `Res_Dem_Arch`
VALUES (6, 'MC/ET/I/64', 4, 2);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
