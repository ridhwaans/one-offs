-- CreateTable
CREATE TABLE "Account" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "username" TEXT NOT NULL
);

-- CreateTable
CREATE TABLE "Topic" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "date_added" DATETIME NOT NULL,
    "account_id" INTEGER NOT NULL,
    FOREIGN KEY ("account_id") REFERENCES "Account" ("id") ON DELETE CASCADE ON UPDATE CASCADE
);

-- CreateTable
CREATE TABLE "Comment" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "account_id" INTEGER NOT NULL,
    "text" TEXT NOT NULL,
    "date_added" DATETIME NOT NULL,
    "topic_id" INTEGER NOT NULL,
    "parent_comment_id" INTEGER,
    "commentId" INTEGER,
    FOREIGN KEY ("account_id") REFERENCES "Account" ("id") ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY ("topic_id") REFERENCES "Topic" ("id") ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY ("commentId") REFERENCES "Comment" ("id") ON DELETE SET NULL ON UPDATE CASCADE
);
