INSERT INTO `Users`(`u_id`, `u_mailaddress`, `u_firstname`, `u_lastname`, `u_username`, `u_password`, `u_sex`,
                    `u_country`, `u_city`, `u_address`, `u_zipcode`)
VALUES (1, 'melody_cjy@163.com', 'Melody', 'CHU', 'Melody CHU', '123456', 1, 'Chine', 'Shanghai', '16 rue Huanlong',
        200125);
INSERT INTO `Users`(`u_id`, `u_mailaddress`, `u_firstname`, `u_lastname`, `u_username`, `u_password`, `u_sex`,
                    `u_country`, `u_city`, `u_address`, `u_zipcode`)
VALUES (2, 'amyshi2016@gmail.com', 'Yanjie', 'SHI', 'Yanjie SHI', '123456', 1, 'France', 'Ivry-sur-Seine',
        '132 boulevard de Stalingrad', 94200);
INSERT INTO `Users`(`u_id`, `u_mailaddress`, `u_firstname`, `u_lastname`, `u_username`, `u_password`, `u_sex`,
                    `u_country`, `u_city`, `u_address`, `u_zipcode`)
VALUES (3, 'floergo@laposte.net', 'Floriane', 'OWXZAREK', 'Floriane OWXZAREK', '123456', 1, 'France', 'Paris',
        '90 rue de Tolbiac', 75013);
INSERT INTO `Users`(`u_id`, `u_mailaddress`, `u_firstname`, `u_lastname`, `u_username`, `u_password`, `u_sex`,
                    `u_country`, `u_city`, `u_address`, `u_zipcode`)
VALUES (4, 'cyril.lacheze@univ-paris1.fr', 'Cyril', 'LACHEZE', 'Cyril LACHEZE', '123456', 0, 'France', 'Paris',
        '90 rue de Tolbiac', 75013);
INSERT INTO `Users`(`u_id`, `u_mailaddress`, `u_firstname`, `u_lastname`, `u_username`, `u_password`, `u_sex`,
                    `u_country`, `u_city`, `u_address`, `u_zipcode`)
VALUES (5, 'exampleuser.01@gmail.com', 'Adam', 'BLACK', 'Adam BLACK', '123456', 1, 'France', 'Marseilles',
        '90 rue de Tolbiac', 75013);
INSERT INTO `Users`(`u_id`, `u_mailaddress`, `u_firstname`, `u_lastname`, `u_username`, `u_password`, `u_sex`,
                    `u_country`, `u_city`, `u_address`, `u_zipcode`)
VALUES (6, 'exampleuser.02@gamil.com', 'Corgi', 'WHITE', 'Corgi WHITE', '123456', 0, 'Allemagne', 'Berlin',
        '28 rue Akazienstraße', 10823);
INSERT INTO `Users`(`u_id`, `u_mailaddress`, `u_firstname`, `u_lastname`, `u_username`, `u_password`, `u_sex`,
                    `u_country`, `u_city`, `u_address`, `u_zipcode`)
VALUES (7, 'exampleuser.03@gmail.com', 'Jean', 'GREEN', 'Jean MICHEAL', '123456', 0, 'Belgique', 'Bruxelles',
        '4 Avenue Palmerston', 1000);
INSERT INTO `Users`(`u_id`, `u_mailaddress`, `u_firstname`, `u_lastname`, `u_username`, `u_password`, `u_sex`,
                    `u_country`, `u_city`, `u_address`, `u_zipcode`)
VALUES (8, 'exampleuser.04@gmail.com', 'Sarah', 'DE LA MARE', 'Sarah DE LA MARE', '123456', 1, 'États-Unis', 'Westmont',
        '921 Pasquinelli Dr', 60559);
INSERT INTO `Users`(`u_id`, `u_mailaddress`, `u_firstname`, `u_lastname`, `u_username`, `u_password`, `u_sex`,
                    `u_country`, `u_city`, `u_address`, `u_zipcode`)
VALUES (9, 'exampleuser.05@gmail.com', 'Annie', 'RAKAN', 'Annie RAKAN', '123456', 1, 'France', 'Paris',
        '90 rue de Tolbiac', 75013);
INSERT INTO `Users`(`u_id`, `u_mailaddress`, `u_firstname`, `u_lastname`, `u_username`, `u_password`, `u_sex`,
                    `u_country`, `u_city`, `u_address`, `u_zipcode`)
VALUES (10, 'exampleuser.06@gmail.com', 'Jack', 'JONES', 'Jack JONES', '123456', 0, 'Grèce', 'Larisa',
        '2 rue Papandreou', 41334);



INSERT INTO `Museum`(`m_ID`, `m_Name`, `m_City`, `m_Address`, `m_ZipCode`, `m_Tel`, `m_Mail`, `m_NbDocumentLimit`,
                     `m_NbVideoLimit`)
VALUES (1, 'Domaine Départemental Pierresvives', 'Montpellier', '907 rue Profesurur Blayac', 34080,
        '(+33) 4 67 67 30 00', ' pierresvives@herault.fr', 17, 17);
INSERT INTO `Museum`(`m_ID`, `m_Name`, `m_City`, `m_Address`, `m_ZipCode`, `m_Tel`, `m_Mail`, `m_NbDocumentLimit`,
                     `m_NbVideoLimit`)
VALUES (2, 'Archives nationales - Site de Pierrefitte-sur-Seine', 'Pierrefitte-sur-Seine', '59 rue Guynemer', 93380,
        '(+33) 1 75 47 20 02', 'archives-nationales@culture.gouv.fr', 12, 12);
INSERT INTO `Museum`(`m_ID`, `m_Name`, `m_City`, `m_Address`, `m_ZipCode`, `m_Tel`, `m_Mail`, `m_NbDocumentLimit`,
                     `m_NbVideoLimit`)
VALUES (3, 'Service des archives - Bureau Régional de Bourgogne-Franche-Comté', 'Besançon',
        '8 Avenue Denfert Rochereau', 25000, '(+33) 3 81 61 61 46', 'odile.boyer@bourgognefranchecomte.fr', 15, 15);
INSERT INTO `Museum`(`m_ID`, `m_Name`, `m_City`, `m_Address`, `m_ZipCode`, `m_Tel`, `m_Mail`, `m_NbDocumentLimit`,
                     `m_NbVideoLimit`)
VALUES (4, 'Service des archives - Bureau Ardeche', 'Privas', 'Place André-Malraux', 7000, '(+33) 4 75 66 98 00',
        'archives@ardeche.fr', 15, 15);
INSERT INTO `Museum`(`m_ID`, `m_Name`, `m_City`, `m_Address`, `m_ZipCode`, `m_Tel`, `m_Mail`, `m_NbDocumentLimit`,
                     `m_NbVideoLimit`)
VALUES (5, 'Service des archives - Bureau Gard', 'Nîmes', '365 rue du Forez', 30000, '(+33) 4 66 05 05 10',
        'archives@gard.fr', 10, 10);
INSERT INTO `Museum`(`m_ID`, `m_Name`, `m_City`, `m_Address`, `m_ZipCode`, `m_Tel`, `m_Mail`, `m_NbDocumentLimit`,
                     `m_NbVideoLimit`)
VALUES (6, 'Service des archives - Bureau Marne', 'Reims', '44 avenue de l\'Yser', 51100, '(+33) 3 26 68 06 69',
        'archives51@marne.fr', 12, 12);
INSERT INTO `Museum`(`m_ID`, `m_Name`, `m_City`, `m_Address`, `m_ZipCode`, `m_Tel`, `m_Mail`, `m_NbDocumentLimit`,
                     `m_NbVideoLimit`)
VALUES (7, 'Service des archives - Bureau Pas-de-Calais', 'Arras', '12 place de la Préfecture', 62000,
        '(+33) 3 21 71 10 90', 'archives62@pasdecalais.fr', 11, 11);
INSERT INTO `Museum`(`m_ID`, `m_Name`, `m_City`, `m_Address`, `m_ZipCode`, `m_Tel`, `m_Mail`, `m_NbDocumentLimit`,
                     `m_NbVideoLimit`)
VALUES (8, 'Service des archives - Bureau Yonne', 'Auxerre', '5 rue Jean-Moulin', 89000, '(+33) 3 86 94 89 00',
        'archives@yonne.fr', 15, 15);
INSERT INTO `Museum`(`m_ID`, `m_Name`, `m_City`, `m_Address`, `m_ZipCode`, `m_Tel`, `m_Mail`, `m_NbDocumentLimit`,
                     `m_NbVideoLimit`)
VALUES (9, 'Service des archives - Bureau Puy-de-Dôme', 'Clermont-Ferrand', '75 rue de Neyrat', 63100,
        '(+33) 4 73 23 45 80', 'archives@puy-de-dome.fr', 14, 14);
INSERT INTO `Museum`(`m_ID`, `m_Name`, `m_City`, `m_Address`, `m_ZipCode`, `m_Tel`, `m_Mail`, `m_NbDocumentLimit`,
                     `m_NbVideoLimit`)
VALUES (10, 'Service des archives - Bureau Pays de la loire', 'Nantes Cedex 9', '1 rue de la Loire', 44966,
        '(+33) 2 28 20 52 48', 'agnes.dejob@paysdelaloire.fr', 17, 17);



INSERT INTO `Archive`(`a_id`, `a_title`, `a_type`, `a_folio`, `a_language`, `a_author`, `a_description`, `museum_id`)
VALUES ('10/EDT/204', 'Construction d\'une tuilerie : correspondance (1630)', 0, NULL, 'Français', 'Aniane',
        'La sous-série 5 S, l\'une des plus riches sur la thématique des commmunications, ne saurait laisser indifférents ceux qui s\'intéressent au développement économique du Languedoc au XIXe siècle. L\'Hérault a d\'ailleurs été l\'un des premiers départements français à posséder une ligne de chemin de fer. La ligne de Montpellier à Sète, projetée dès 1834, entreprise en 1837, était en service en 1839. Les dossiers d\'enquête, préalables à la mise en oeuvre des voies ferrées, recèlent de nombreux renseignements d\'ordre économique, notamment sur la production viticole et minière, le commerce et le roulage sur les routes destinées à être doublées par le chemin de fer. Les premiers tronçons ont été conçus dans un intérêt purement local, d\'où des études sur le trafic routier et la rentabilité des lignes. Ils contiennent aussi des délibérations, pétitions, interventions, etc., relatives au choix du tracé des lignes. On y trouve en outre de nombreux renseignements sur l\'urbanisme des grandes villes, sur le choix de l\'emplacement des gares de Montpellier (5 S 72-76, 615-621), sur l\'agrandissement du port de Sète (5 S 63, 126-130, 164-168), sur les déraillements, les pannes et les accidents qui arrivent fréquemment au cours des premières années d\'exploitation ; sur les inévitables procès entraînés par tous les grands travaux publics. Le contentieux de l\'intérêt local compte à lui seul plus de 18 gros dossiers (5 S 427-440, 1386-1389). Mentionnons, pour finir, l\'abondante documentation sur le matériel ferroviaire, dans les réseaux d\'intérêt général ou local et dans les tramways.',
        1);
INSERT INTO `Archive`(`a_id`, `a_title`, `a_type`, `a_folio`, `a_language`, `a_author`, `a_description`, `museum_id`)
VALUES ('105/FI/1337',
        'Une des photographies composant le fonds Lunais-Bruère : le centre-ville de Blois après les destructions de la seconde guerre mondiale. Négatif stéréoscopique',
        2, NULL, 'Français', 'Fr',
        'Les documents donnés par cette famille blésoise illustrent parfaitement les soubresauts de la première moitié du XXe siècle : journaux intimes d’un abbé sous l’Occupation, lettres adressés à ses parents par un jeune homme effectuant son service du travail obligatoire (STO), papiers concernant la participation à des jeunesses catholiques féminines, etc. Accompagné d’une collection très riche de photographies et de plaques de verres, ce fonds permet de se plonger au cœur d’une famille : au-delà de l’aspect patrimonial, il s’agit d’une source précieuse pour étudier la vie quotidienne et les relations sociales sur une période de plus de 60 ans.',
        7);
INSERT INTO `Archive`(`a_id`, `a_title`, `a_type`, `a_folio`, `a_language`, `a_author`, `a_description`, `museum_id`)
VALUES ('122/J/1273',
        'Projet de création d\'un \"centre de congrès et de rencontres\" en lieu et place de la Halle aux grains à Blois (carnet de croquis, 1975-1976)',
        2, 129, 'Français', 'Fr',
        'Les dossiers de travaux et les plans de ce cabinet d’architecture constituent un ensemble unique à l’échelle du Blésois. Couvrant toute la seconde moitié du XXe siècle, il renferme certains grands projets architecturaux ou urbanistiques (le projet abandonné de construction d’une salle de spectacle à la place de la Halle aux Grains de Blois par exemple). Le fonds offre également une large panoplie de chantiers de moindre envergure mais non moins significatifs (en particulier les travaux de rénovation du vieux Blois, auxquels MM. Aubry et Ferrieux participèrent activement).',
        3);
INSERT INTO `Archive`(`a_id`, `a_title`, `a_type`, `a_folio`, `a_language`, `a_author`, `a_description`, `museum_id`)
VALUES ('19770932/1', 'Service des chemins de fer - Sous-direction des transports ferroviaires (1938-1960)', 0, NULL,
        'Français', 'Sous-direction des transports ferroviaires',
        'Les dossiers portant les numéros TT 27L à TT 282, concernent l\'électrification des chemins de fer entre 1938 et 1960. Il s\'agit de dossiers, probablement incomplets, retrouvés dans le local de la mission des Archives Nationales du Ministère des Travaux Publics.\n\nIl n\'a pas été possible à la mission de réunir une documentation sur l\'historique de l\'électrification des chemins de fer. Une étude devra être faite au moment du triage de l\'ensemble des archives du service des chemins de fer dont une grande partie est conservée sans inventaire dans une cave du 246 boulevard Saint-Germain',
        2);
INSERT INTO `Archive`(`a_id`, `a_title`, `a_type`, `a_folio`, `a_language`, `a_author`, `a_description`, `museum_id`)
VALUES ('30/FI/1/34', 'Le château de La Ferté-Imbault : aquarelle de Louis de La Saussaye, 8 août 1832', 1, NULL,
        'Français', 'Château de La Ferté-Imbault',
        'Cet ensemble de documents, couvrant la période 1341-1891, est un bon exemple de ce que sont les archives des familles aristocratiques. En plus des papiers de gestion du domaine (baux, acquêts, fois et hommages, pièces de procédures judiciaires…), on y trouve nombre de pièces relatives à des branches plus ou moins éloignées de la famille (en particulier la famille d’Estampes). Le travail d’indexation par l’archiviste est ici essentiel pour que la recherche s’effectue à la fois par personne et par localité.',
        3);
INSERT INTO `Archive`(`a_id`, `a_title`, `a_type`, `a_folio`, `a_language`, `a_author`, `a_description`, `museum_id`)
VALUES ('MC/ET/I/64',
        'Marché de Sasbout de Varicq, gentilhomme hollandais, demeurant à la Tuilerie du Pré-aux-Clercs, 9 février 1608',
        0, NULL, 'Français', 'Germain TRONSON',
        '1608 : janvier à avril, juin, août, octobre et décembre. 1608, 24 avril : copie . Sur la couverture, note de Germain Tronson indiquant qu\'en raison de son association avec Germain Desmarquets (ET/LVIII) au commencement d\'avril, les autres mois sont dans la pratique de celui-ci.',
        2);
INSERT INTO `Archive`(`a_id`, `a_title`, `a_type`, `a_folio`, `a_language`, `a_author`, `a_description`, `museum_id`)
VALUES ('MC/ET/XXXIII/23',
        'Minutes et répertoires du notaire Yves BOURGEOIS, 20 septembre 1539 - 26 août 1549 (étude XXXIII)', 0, 492,
        'Français', 'Yves BOURGEOIS',
        'Minutes et répertoires : la loi 2008-696 du 15 juillet 2008 relative aux archives a fixé à 75 ans à compter de la date de l\'acte, ou à 25 ans à compter de la date du décès de l\'intéressé si ce délai est plus bref, le délai de communication des minutes et répertoires des notaires ; ce délai est porté à 100 ans à compter de la date de l\'acte si le document se rapporte à un mineur (code du Patrimoine, articles L213-2, 4e d et 5e).\n\n',
        5);



INSERT INTO `Reservation`(`r_id`, `r_enddate`, `r_status`, `r_providerhassent`, `r_demanderhasreceived`, `r_creator_id`,
                          `r_museum_id`)
VALUES (1, '2021-03-01', 1, 1, 1, 2, 4);
INSERT INTO `Reservation`(`r_id`, `r_enddate`, `r_status`, `r_providerhassent`, `r_demanderhasreceived`, `r_creator_id`,
                          `r_museum_id`)
VALUES (2, '2021-03-04', 1, 1, 0, 6, 7);
INSERT INTO `Reservation`(`r_id`, `r_enddate`, `r_status`, `r_providerhassent`, `r_demanderhasreceived`, `r_creator_id`,
                          `r_museum_id`)
VALUES (3, '2021-03-19', 0, 0, 0, 3, 2);
INSERT INTO `Reservation`(`r_id`, `r_enddate`, `r_status`, `r_providerhassent`, `r_demanderhasreceived`, `r_creator_id`,
                          `r_museum_id`)
VALUES (4, '2021-03-20', 0, 0, 0, 2, 2);



INSERT INTO `Res_Dem_Arch`(`rad_id`, `archive_id`, `reservation_id`, `resv_user_id`)
VALUES (1, '10/EDT/204', 1, 1);
INSERT INTO `Res_Dem_Arch`(`rad_id`, `archive_id`, `reservation_id`, `resv_user_id`)
VALUES (2, '10/EDT/204', 3, 7);
INSERT INTO `Res_Dem_Arch`(`rad_id`, `archive_id`, `reservation_id`, `resv_user_id`)
VALUES (3, '122/J/1273', 3, 4);
INSERT INTO `Res_Dem_Arch`(`rad_id`, `archive_id`, `reservation_id`, `resv_user_id`)
VALUES (4, '122/J/1273', 2, 6);
INSERT INTO `Res_Dem_Arch`(`rad_id`, `archive_id`, `reservation_id`, `resv_user_id`)
VALUES (5, '105/FI/1337', 3, 5);
INSERT INTO `Res_Dem_Arch`(`rad_id`, `archive_id`, `reservation_id`, `resv_user_id`)
VALUES (6, 'MC/ET/I/64', 4, 2);
