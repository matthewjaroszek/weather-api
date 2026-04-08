CREATE TABLE locations (
    locations_id INTEGER PRIMARY KEY,
    country TEXT NOT NULL,
    location_name TEXT NOT NULL,
    latitude NUMERIC(8,2) NOT NULL,
    longitude NUMERIC(8,2) NOT NULL,
    timezone TEXT NOT NULL,
    UNIQUE (country, location_name, latitude, longitude, timezone)
);

CREATE TABLE weather_observations (
    weather_observations_id INTEGER PRIMARY KEY,
    locations_id BIGINT NOT NULL
        REFERENCES locations(locations_id)
        ON DELETE CASCADE,

    last_updated_epoch BIGINT NOT NULL,
    temperature_fahrenheit NUMERIC(5,1),
    condition_text TEXT,
    wind_mph NUMERIC(5,1),
    wind_degree SMALLINT CHECK (wind_degree BETWEEN 0 AND 360),
    wind_direction VARCHAR(3),
    pressure_mb NUMERIC(6,1),
    precip_in NUMERIC(5,2),
    humidity SMALLINT CHECK (humidity BETWEEN 0 AND 100),
    cloud SMALLINT CHECK (cloud BETWEEN 0 AND 100),
    feels_like_fahrenheit NUMERIC(5,1),
    visibility_miles NUMERIC(5,1),
    uv_index NUMERIC(4,1),
    gust_mph NUMERIC(5,1),
    UNIQUE (locations_id, last_updated_epoch)
);

CREATE TABLE air_quality_observations (
    weather_observations_id BIGINT PRIMARY KEY
        REFERENCES weather_observations(weather_observations_id)
        ON DELETE CASCADE,
    air_quality_carbon_monoxide NUMERIC(10,1),
    air_quality_ozone NUMERIC(10,1),
    air_quality_nitrogen_dioxide NUMERIC(10,1),
    air_quality_sulphur_dioxide NUMERIC(10,1),
    air_quality_pm2_5 NUMERIC(10,1),
    air_quality_pm10 NUMERIC(10,1),
    air_quality_us_epa_index SMALLINT,
    air_quality_gb_defra_index SMALLINT
);

CREATE TABLE astronomy_observations (
    weather_observations_id BIGINT PRIMARY KEY
        REFERENCES weather_observations(weather_observations_id)
        ON DELETE CASCADE,
    sunrise TIME,
    sunset TIME,
    moonrise TIME,
    moonset TIME,
    moon_phase TEXT,
    moon_illumination SMALLINT CHECK (moon_illumination BETWEEN 0 AND 100)
);

CREATE INDEX idx_weather_location_time
    ON weather_observations (locations_id, last_updated_epoch);