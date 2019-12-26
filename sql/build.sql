--
-- Create model Company
--
CREATE TABLE `company_company` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `uniform_social_credit_code` varchar(18) NOT NULL, `name` varchar(128) NOT NULL, `registered_capital` varchar(64) NOT NULL, `paid_up_capital` varchar(64) NOT NULL, `business_scope` varchar(1024) NOT NULL, `industry` varchar(128) NOT NULL, `tel` varchar(64) NOT NULL, `email` varchar(254) NOT NULL, `province` varchar(32) NOT NULL, `city` varchar(32) NOT NULL, `district` varchar(32) NOT NULL, `detail_address` varchar(128) NOT NULL, `company_type` varchar(128) NOT NULL, `business_registration_number` varchar(14) NOT NULL, `registration_authority` varchar(128) NOT NULL, `operating_status` varchar(64) NOT NULL);
--
-- Create model Trademark
--
CREATE TABLE `company_trademark` (`id` varchar(16) NOT NULL PRIMARY KEY, `image_url` varchar(200) NOT NULL, `name` varchar(128) NOT NULL, `company_id` integer NOT NULL);
--
-- Create model Classification
--
CREATE TABLE `company_classification` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `classification` varchar(64) NOT NULL, `process` varchar(64) NOT NULL, `status` varchar(16) NOT NULL, `trademark_id` varchar(16) NOT NULL);
--
-- Create model Change
--
CREATE TABLE `company_change` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `change_date` date NOT NULL, `change_item` varchar(64) NOT NULL, `before_change` varchar(1024) NOT NULL, `after_change` varchar(1024) NOT NULL, `create_date` date NOT NULL, `company_id` integer NOT NULL);
ALTER TABLE `company_trademark` ADD CONSTRAINT `company_trademark_company_id_e48478b9_fk_company_company_id` FOREIGN KEY (`company_id`) REFERENCES `company_company` (`id`);
ALTER TABLE `company_classification` ADD CONSTRAINT `company_classificati_trademark_id_b4ae8983_fk_company_t` FOREIGN KEY (`trademark_id`) REFERENCES `company_trademark` (`id`);
ALTER TABLE `company_change` ADD CONSTRAINT `company_change_company_id_1b5d6ee5_fk_company_company_id` FOREIGN KEY (`company_id`) REFERENCES `company_company` (`id`);
--
-- Create model Serving
--
CREATE TABLE `human_serving` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `human_name` varchar(32) NOT NULL, `position` varchar(32) NOT NULL, `company_id` integer NOT NULL);
ALTER TABLE `human_serving` ADD CONSTRAINT `human_serving_company_id_38456fd3_fk_company_company_id` FOREIGN KEY (`company_id`) REFERENCES `company_company` (`id`);
