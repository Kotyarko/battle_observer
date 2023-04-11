#define configs_dir "{app}\mods\configs\mod_battle_observer"
#define mod_source "..\..\output_data\mods"
#define configs "..\..\output_data\configs\mod_battle_observer"

[Types]
Name: "armagomen"; Description: {cm:types_armagomen};
Name: "user"; Description: {cm:types_user}; Flags: iscustom; 

//
[Components]
Name: debug_panel; Description: {cm:debug_panel}; Types: "armagomen";
//Name: debug_panel/minimal; Description: {cm:debug_panel};
//Name: debug_panel/modern; Description: {cm:debug_panel};

Name: sixth_sense; Description: {cm:sixth_sense}; Flags: disablenouninstallwarning; Types: "armagomen";
Name: arcade_camera; Description: {cm:arcade_camera}; Flags: disablenouninstallwarning; Types: "armagomen";
Name: armor_calculator; Description: {cm:armor_calculator}; Flags: disablenouninstallwarning; Types: "armagomen";
Name: avg_efficiency_in_hangar; Description: {cm:avg_efficiency_in_hangar}; Flags: disablenouninstallwarning; Types: "armagomen";
Name: battle_timer; Description: {cm:battle_timer}; Flags: disablenouninstallwarning; Types: "armagomen";
Name: clock; Description: {cm:clock}; Flags: disablenouninstallwarning; Types: "armagomen";
Name: dispersion_circle; Description: {cm:dispersion_circle}; Flags: disablenouninstallwarning; Types: "armagomen";
Name: dispersion_timer; Description: {cm:dispersion_timer}; Flags: disablenouninstallwarning; Types: "armagomen";
Name: distance_to_enemy; Description: {cm:distance_to_enemy}; Flags: disablenouninstallwarning;
Name: effects; Description: {cm:effects}; Flags: disablenouninstallwarning; Types: "armagomen";
Name: flight_time; Description: {cm:flight_time}; Flags: disablenouninstallwarning; Types: "armagomen";
Name: hp_bars; Description: {cm:hp_bars}; Flags: disablenouninstallwarning; Types: "armagomen";
Name: log_extended; Description: {cm:log_extended}; Flags: disablenouninstallwarning; Types: "armagomen";
Name: log_total; Description: {cm:log_total}; Flags: disablenouninstallwarning; Types: "armagomen";
Name: main; Description: {cm:main}; Flags: disablenouninstallwarning; Types: "armagomen";
Name: main_gun; Description: {cm:main_gun}; Flags: disablenouninstallwarning; Types: "armagomen";
Name: minimap; Description: {cm:minimap}; Flags: disablenouninstallwarning; Types: "armagomen";
Name: own_health; Description: {cm:own_health}; Flags: disablenouninstallwarning;
Name: players_panels; Description: {cm:players_panels}; Flags: disablenouninstallwarning; Types: "armagomen";
Name: service_channel_filter; Description: {cm:service_channel_filter}; Flags: disablenouninstallwarning; Types: "armagomen";
Name: statistics; Description: {cm:statistics}; Flags: disablenouninstallwarning; Types: "armagomen";
Name: strategic_camera; Description: {cm:strategic_camera}; Flags: disablenouninstallwarning; Types: "armagomen";
Name: tank_carousel; Description: {cm:tank_carousel}; Flags: disablenouninstallwarning;
Name: team_bases_panel; Description: {cm:team_bases_panel}; Flags: disablenouninstallwarning; Types: "armagomen";
Name: wg_logs; Description: {cm:wg_logs}; Flags: disablenouninstallwarning;
Name: zoom; Description: {cm:zoom}; Flags: disablenouninstallwarning; Types: "armagomen";


[Files]
Source: "{#mod_source}\*"; DestDir: "{app}\{code:PH_Folder_Mods}"; Flags: ignoreversion;
Source: "{#configs}\load.json"; DestDir: "{#configs_dir}"; Flags: ignoreversion;
Source: "{#configs}\armagomen\debug_panel.json"; DestDir: "{#configs_dir}\armagomen"; Flags: ignoreversion; Components: debug_panel;
Source: "{#configs}\armagomen\sixth_sense.json"; DestDir: "{#configs_dir}\armagomen"; Flags: ignoreversion; Components: sixth_sense;
Source: "{#configs}\armagomen\arcade_camera.json"; DestDir: "{#configs_dir}\armagomen"; Flags: ignoreversion; Components: arcade_camera;
Source: "{#configs}\armagomen\armor_calculator.json"; DestDir: "{#configs_dir}\armagomen"; Flags: ignoreversion; Components: armor_calculator;
Source: "{#configs}\armagomen\avg_efficiency_in_hangar.json"; DestDir: "{#configs_dir}\armagomen"; Flags: ignoreversion; Components: avg_efficiency_in_hangar;
Source: "{#configs}\armagomen\battle_timer.json"; DestDir: "{#configs_dir}\armagomen"; Flags: ignoreversion; Components: battle_timer;
Source: "{#configs}\armagomen\clock.json"; DestDir: "{#configs_dir}\armagomen"; Flags: ignoreversion; Components: clock;
Source: "{#configs}\armagomen\dispersion_circle.json"; DestDir: "{#configs_dir}\armagomen"; Flags: ignoreversion; Components: dispersion_circle;
Source: "{#configs}\armagomen\dispersion_timer.json"; DestDir: "{#configs_dir}\armagomen"; Flags: ignoreversion; Components: dispersion_timer;
Source: "{#configs}\armagomen\distance_to_enemy.json"; DestDir: "{#configs_dir}\armagomen"; Flags: ignoreversion; Components: distance_to_enemy;
Source: "{#configs}\armagomen\effects.json"; DestDir: "{#configs_dir}\armagomen"; Flags: ignoreversion; Components: effects;
Source: "{#configs}\armagomen\flight_time.json"; DestDir: "{#configs_dir}\armagomen"; Flags: ignoreversion; Components: flight_time;
Source: "{#configs}\armagomen\hp_bars.json"; DestDir: "{#configs_dir}\armagomen"; Flags: ignoreversion; Components: hp_bars;
Source: "{#configs}\armagomen\log_extended.json"; DestDir: "{#configs_dir}\armagomen"; Flags: ignoreversion; Components: log_extended;
Source: "{#configs}\armagomen\log_total.json"; DestDir: "{#configs_dir}\armagomen"; Flags: ignoreversion; Components: log_total;
Source: "{#configs}\armagomen\main.json"; DestDir: "{#configs_dir}\armagomen"; Flags: ignoreversion; Components: main;
Source: "{#configs}\armagomen\main_gun.json"; DestDir: "{#configs_dir}\armagomen"; Flags: ignoreversion; Components: main_gun;
Source: "{#configs}\armagomen\minimap.json"; DestDir: "{#configs_dir}\armagomen"; Flags: ignoreversion; Components: minimap;
Source: "{#configs}\armagomen\own_health.json"; DestDir: "{#configs_dir}\armagomen"; Flags: ignoreversion; Components: own_health;
Source: "{#configs}\armagomen\players_panels.json"; DestDir: "{#configs_dir}\armagomen"; Flags: ignoreversion; Components: players_panels;
Source: "{#configs}\armagomen\service_channel_filter.json"; DestDir: "{#configs_dir}\armagomen"; Flags: ignoreversion; Components: service_channel_filter;
Source: "{#configs}\armagomen\statistics.json"; DestDir: "{#configs_dir}\armagomen"; Flags: ignoreversion; Components: statistics;
Source: "{#configs}\armagomen\strategic_camera.json"; DestDir: "{#configs_dir}\armagomen"; Flags: ignoreversion; Components: strategic_camera;
Source: "{#configs}\armagomen\tank_carousel.json"; DestDir: "{#configs_dir}\armagomen"; Flags: ignoreversion; Components: tank_carousel;
Source: "{#configs}\armagomen\team_bases_panel.json"; DestDir: "{#configs_dir}\armagomen"; Flags: ignoreversion; Components: team_bases_panel;
Source: "{#configs}\armagomen\wg_logs.json"; DestDir: "{#configs_dir}\armagomen"; Flags: ignoreversion; Components: wg_logs;
Source: "{#configs}\armagomen\zoom.json"; DestDir: "{#configs_dir}\armagomen"; Flags: ignoreversion; Components: zoom;

