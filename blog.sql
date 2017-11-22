PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
--CREATE TABLE "blog_article" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(200) NOT NULL, "authors_name" varchar(200) NOT NULL, "content" text NOT NULL, "published" bool NOT NULL, "posted_date" datetime NOT NULL);
INSERT INTO "blog_article" VALUES(1,'Sports','Mr. Bean','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse massa orci, scelerisque non nisi quis, bibendum tincidunt justo. Mauris id sollicitudin ipsum, a lobortis eros. Pellentesque ullamcorper neque libero, non varius
                        diam vehicula in. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse vitae felis ligula. Curabitur ac nulla vitae leo ornare auctor a nec turpis. Fusce semper pellentesque velit, non molestie ante pretium cursus.
                        Vivamus quam nibh, placerat sit amet est eu, tincidunt bibendum lacus.',1,'2017-11-21 08:05:07.077426');
INSERT INTO "blog_article" VALUES(2,'Music','Not Mr. Bean','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse massa orci, scelerisque non nisi quis, bibendum tincidunt justo. Mauris id sollicitudin ipsum, a lobortis eros. Pellentesque ullamcorper neque libero, non varius
                        diam vehicula in. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse vitae felis ligula. Curabitur ac nulla vitae leo ornare auctor a nec turpis. Fusce semper pellentesque velit, non molestie ante pretium cursus.
                        Vivamus quam nibh, placerat sit amet est eu, tincidunt bibendum lacus.',1,'2017-11-21 08:05:26.742977');
INSERT INTO "blog_article" VALUES(3,'Life','Whos this','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse massa orci, scelerisque non nisi quis, bibendum tincidunt justo. Mauris id sollicitudin ipsum, a lobortis eros. Pellentesque ullamcorper neque libero, non varius
                        diam vehicula in. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse vitae felis ligula. Curabitur ac nulla vitae leo ornare auctor a nec turpis. Fusce semper pellentesque velit, non molestie ante pretium cursus.
                        Vivamus quam nibh, placerat sit amet est eu, tincidunt bibendum lacus.',1,'2017-11-21 08:05:46.195347');
INSERT INTO "blog_article" VALUES(4,'Family','Yours Truly','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse massa orci, scelerisque non nisi quis, bibendum tincidunt justo. Mauris id sollicitudin ipsum, a lobortis eros. Pellentesque ullamcorper neque libero, non varius
                        diam vehicula in. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse vitae felis ligula. Curabitur ac nulla vitae leo ornare auctor a nec turpis. Fusce semper pellentesque velit, non molestie ante pretium cursus.
                        Vivamus quam nibh, placerat sit amet est eu, tincidunt bibendum lacus.',1,'2017-11-21 08:06:05.819525');
COMMIT;
