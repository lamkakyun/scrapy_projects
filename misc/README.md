```
CREATE TABLE IF NOT EXISTS ip_pool (
        ip_port    CHAR (20) PRIMARY KEY,
        is_https   INT (1),
        hide_level INT (2),
        fail_num   INT (4)   DEFAULT (0),
        uptime     INT (11) 
        );
```