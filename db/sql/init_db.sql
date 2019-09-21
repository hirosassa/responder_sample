DROP TABLE IF EXISTS test_user;

CREATE TABLE IF NOT EXISTS test_user (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(30) NOT NULL,
  specialty VARCHAR(30) DEFAULT NULL,
  created_at DATETIME DEFAULT current_timestamp,
  updated_at DATETIME DEFAULT current_timestamp ON UPDATE current_timestamp
);

INSERT INTO test_user (name, specialty) VALUES
('jone_doe', 'cardiology'),
('jane_doe', 'oncology');
