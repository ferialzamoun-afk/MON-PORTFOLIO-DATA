
CREATE TABLE Region (
                Code_dep_code_commune VARCHAR NOT NULL,
                reg_code INTEGER NOT NULL,
                reg_nom VARCHAR(30) NOT NULL,
                aca_nom VARCHAR(50) NOT NULL,
                dep_nom VARCHAR(50) NOT NULL,
                com_nom_maj_court VARCHAR(30) NOT NULL,
                dep_code INTEGER NOT NULL,
                dep_nom_num VARCHAR NOT NULL,
                CONSTRAINT Region_pk PRIMARY KEY (Code_dep_code_commune)
);
COMMENT ON COLUMN Region.reg_code IS 'Code département  y  compris Collectivités d''outre-mer';
COMMENT ON COLUMN Region.reg_nom IS 'Liste prédéfinie de 20 noms de régions françaises';
COMMENT ON COLUMN Region.aca_nom IS 'Liste prédéfinie de 37 noms de chef-lieu  1  pour chaque région reg_nom';
COMMENT ON COLUMN Region.dep_nom IS 'Liste prédéfinie de 113 noms de département';
COMMENT ON COLUMN Region.com_nom_maj_court IS 'Liste de nom court de commune mis à jour';
COMMENT ON COLUMN Region.dep_code IS 'Numéro du département';
COMMENT ON COLUMN Region.dep_nom_num IS 'Concaténation du dep_nom avec le "("+ code département +")"';


CREATE TABLE Contrat (
                Contrat_ID INTEGER NOT NULL,
                No_voie INTEGER NOT NULL,
                B_T_Q CHAR(1) NOT NULL,
                Type_de_voie VARCHAR NOT NULL,
                Voie VARCHAR NOT NULL,
                Code_dep_code_commune VARCHAR NOT NULL,
                Code_postal INTEGER NOT NULL,
                Surface INTEGER NOT NULL,
                Occupation VARCHAR NOT NULL,
                Prix_cotisation_mensuel INTEGER NOT NULL,
                Valeur_declaree_biens VARCHAR(11) NOT NULL,
                Formule VARCHAR NOT NULL,
                Type_local VARCHAR NOT NULL,
                Type_contrat VARCHAR NOT NULL,
                CONSTRAINT Contrat_pk PRIMARY KEY (Contrat_ID)
);
COMMENT ON COLUMN Contrat.Contrat_ID IS 'Id unique pour les contrats';
COMMENT ON COLUMN Contrat.B_T_Q IS 'Indicateur éventuel de répétition pour l''adresse du logement assuré sur un caractère';
COMMENT ON COLUMN Contrat.Voie IS 'Libellé de la voie pour l''adresse du logement assuré';
COMMENT ON COLUMN Contrat.Code_postal IS 'Code postal pour l''adresse du logement assuré';
COMMENT ON COLUMN Contrat.Surface IS 'Nombre en Mètre carré de surface habitable';
COMMENT ON COLUMN Contrat.Occupation IS 'Liste prédéfinie "Locataire" ou "Propriétaire"';
COMMENT ON COLUMN Contrat.Prix_cotisation_mensuel IS 'Nombre de 1 à 3 chiffres';
COMMENT ON COLUMN Contrat.Valeur_declaree_biens IS 'Liste prédéfiniede 4 items : "0-25000", "25000-50000","50000+","100000+"';
COMMENT ON COLUMN Contrat.Formule IS 'Liste prédéfinie : "Integral"  ou "Classique"';
COMMENT ON COLUMN Contrat.Type_contrat IS 'Liste prédéfinie: "Residence principale","Residence secondaire", "Mise en location"';


ALTER TABLE Contrat ADD CONSTRAINT Region_Contrat_fk
FOREIGN KEY (Code_dep_code_commune)
REFERENCES Region (Code_dep_code_commune)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;
