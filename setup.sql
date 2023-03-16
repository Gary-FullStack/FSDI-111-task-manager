CREATE TABLE status (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(128)
);  

CREATE TABLE task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    summary VARCHAR(256),
    description TEXT,
    status_id INTEGER,
    active BOOLEAN DEFAULT 1,
    FOREIGN KEY (status_id) REFERENCES status(id)
);


INSERT INTO status ( name ) VALUES ("to do");
INSERT INTO status ( name ) VALUES ("in progress");
INSERT INTO status ( name ) VALUES ("done");


INSERT INTO task (
    summary,
    description,
    status_id
) VALUES (
    "Do some stuff",
    " Put stuff over there",
    1
);

INSERT INTO task (
    summary,
    description,
    status_id
) VALUES (
    "Mow the lawn",
    "Don't run over the roses this time",
    1
);

INSERT INTO task (
    summary,
    description,
    status_id
) VALUES (
    "wash the car",
    "Use only dehydrated water",
    1
);