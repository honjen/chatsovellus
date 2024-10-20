INSERT INTO categories (name) VALUES ('kissat');
INSERT INTO categories (name) VALUES ('koirat');
INSERT INTO categories (name) VALUES ('kissat vs koirat');

INSERT INTO threads (user_id, category_id, name, content) VALUES (1, 1, 'Mikä on lempi kissarotusi?', 'En muista nimeä, mutta ne karvattomat kissat on tosi söpöjä. Kertokaa mistä te tykkäätte.');
INSERT INTO threads (user_id, category_id, name, content) VALUES (1, 1, 'Parhaat kissavideot', 'Tiedätte jo varmaan angrycat:in. Antakaa videovinkkejä :)');
INSERT INTO threads (user_id, category_id, name, content) VALUES (1, 2, 'Söpöimmät koirat', 'Huskyt on ihania <3 Mitkä muut koirarodut on hyviä?');
INSERT INTO threads (user_id, category_id, name, content) VALUES (1, 2, 'Kerro koirastasi', 'Mun koira aina kerjää juustoa jos huomaa, että käyn jääkaapilla. Minkälaisia teidän koirat on?');
INSERT INTO threads (user_id, category_id, name, content) VALUES (1, 3, 'Kummat on parempii: kissat vai koirat', 'Mun mielestä molemmat on ihania, mut mitä mieltä te ootte?');
INSERT INTO threads (user_id, category_id, name, content) VALUES (1, 3, 'Koirat on kivempii ku kissat', 'Sehän on vain ihan ilmiselvää et koirat on parempii lemmikkejä :D');

INSERT INTO messages (thread_id, user_id, category_id, content) VALUES (1, 1, 1, 'En mä tiedä. Ne on kaikki niin söpöjä.');
INSERT INTO messages (thread_id, user_id, category_id, content) VALUES (1, 1, 1, 'Totta :D.');
INSERT INTO messages (thread_id, user_id, category_id, content) VALUES (2, 1, 1, 'Ootteko nähny sen missä se kissa soittaa pianoa?');
INSERT INTO messages (thread_id, user_id, category_id, content) VALUES (2, 1, 1, 'Se on just paras.');
INSERT INTO messages (thread_id, user_id, category_id, content) VALUES (3, 1, 2, 'Shibat on söpöimpiä mun mielestä.');
INSERT INTO messages (thread_id, user_id, category_id, content) VALUES (3, 1, 2, 'Mä tykkään pugeista.');
INSERT INTO messages (thread_id, user_id, category_id, content) VALUES (4, 1, 2, 'Meidän koira nukkuu mun sängyssä vaikka vanhemmat sanoo ettei sais :D');
INSERT INTO messages (thread_id, user_id, category_id, content) VALUES (4, 1, 2, 'Meidän koira juo vessasta vettä välillä :/');
INSERT INTO messages (thread_id, user_id, category_id, content) VALUES (5, 1, 3, 'Kissoja on helpompaa pitää lemmikkeinä ku ei tarvii kävellyttää.');
INSERT INTO messages (thread_id, user_id, category_id, content) VALUES (5, 1, 3, 'Mut koirat on niin lojaaleja ja sulosia.');
INSERT INTO messages (thread_id, user_id, category_id, content) VALUES (6, 1, 3, 'Eikä oo! Kissat on omalla tavallaan ihania.');
INSERT INTO messages (thread_id, user_id, category_id, content) VALUES (6, 1, 3, 'Agree to disagree.');