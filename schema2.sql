INSERT INTO categories (name) VALUES ('kissat');
INSERT INTO categories (name) VALUES ('koirat');
INSERT INTO categories (name) VALUES ('kissat vs koirat');

INSERT INTO threads (user_id, category_id, name) VALUES (1, 1, 'Mikä on lempi kissarotusi?');
INSERT INTO threads (user_id, category_id, name) VALUES (1, 1, 'Parhaat kissavideot');
INSERT INTO threads (user_id, category_id, name) VALUES (1, 2, 'Söpöimmät koirat');
INSERT INTO threads (user_id, category_id, name) VALUES (1, 2, 'Kerro koirastasi');
INSERT INTO threads (user_id, category_id, name) VALUES (1, 3, 'Kummat on parempii: kissat vai koirat');
INSERT INTO threads (user_id, category_id, name) VALUES (1, 3, 'Koirat on kivempii ku kissat');

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