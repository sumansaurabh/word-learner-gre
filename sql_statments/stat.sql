/*
* @Author: sumansaurabh
* @Date:   2018-06-29 22:29:01
* @Last Modified by:   sumansaurabh
* @Last Modified time: 2018-06-29 22:31:11
*/

ALTER TABLE Words
ADD COLUMN word_type VARCHAR(10);


UPDATE Words
SET word_type = "baron";