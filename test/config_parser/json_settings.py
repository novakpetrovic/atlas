import collections
import json

class JsonSettings:

    def __init__(self):
        self.settings = collections.defaultdict()
        with open('portfolio_linux.json', 'r') as settings:
            ext_settings = json.load(settings)
            self.settings['atlas_settings_file'] = ext_settings['atlas_settings_file']
            self.settings['atlas_session_file'] = ext_settings['atlas_session_file']
            self.settings['portfolio_base_dir'] = ext_settings['portfolio_base_dir']
            self.settings['portfolio_files'] = [self.settings['portfolio_base_dir'] + f for f in ext_settings['portfolio_files']]
            self.settings['portfolio_log_file'] = self.settings['portfolio_base_dir'] + ext_settings['portfolio_log_file']
            self.settings['earned_times_file'] = self.settings['portfolio_base_dir'] + ext_settings['earned_times_file']
            self.settings['backup_dir'] = ext_settings['backup_dir']
            self.settings['daily_files_archive_dir'] = ext_settings['daily_files_archive_dir']
            self.settings['daily_file'] = self.settings['portfolio_base_dir'] + ext_settings['daily_file']
            self.settings['booked_file'] = self.settings['portfolio_base_dir'] + ext_settings['booked_file']
            self.settings['periodic_file'] = self.settings['portfolio_base_dir'] + ext_settings['periodic_file']
            self.settings['shlist_file'] = self.settings['portfolio_base_dir'] + ext_settings['shlist_file']
            self.settings['today_file'] = self.settings['portfolio_base_dir'] + ext_settings['today_file']
            self.settings['tab_order'] = [self.settings['portfolio_base_dir'] + f for f in ext_settings['tab_order']]
            self.settings['tokens_in_sorting_order'] = ext_settings['tokens_in_sorting_order']
            self.settings['space'] = ext_settings['space']
            self.settings['heading_prefix'] = ext_settings['heading_prefix']
            self.settings['ttl_heading'] = ext_settings['ttl_heading']
            self.settings['incoming_heading'] = ext_settings['incoming_heading']
            self.settings['tasks_proposed_heading'] = ext_settings['tasks_proposed_heading']
            self.settings['tasks_done_heading'] = ext_settings['tasks_done_heading']
            self.settings['the_end_heading'] = ext_settings['the_end_heading']
            self.settings['special_heading_suffix'] = ext_settings['special_heading_suffix']
            self.settings['due_prop'] = ext_settings['due_prop']
            self.settings['dur_prop'] = ext_settings['dur_prop']
            self.settings['rec_prop'] = ext_settings['rec_prop']
            self.settings['daily_rec_prop_val'] = ext_settings['daily_rec_prop_val']
            self.settings['tag_prefix'] = ext_settings['tag_prefix']
            self.settings['work_tag'] = ext_settings['work_tag']
            self.settings['incoming_tag'] = ext_settings['incoming_tag']
            self.settings['cat_prefix'] = ext_settings['cat_prefix']
            self.settings['shlist_cat'] = ext_settings['shlist_cat']
            self.settings['top_task_prefix'] = ext_settings['top_task_prefix']
            self.settings['open_task_prefix'] = ext_settings['open_task_prefix']
            self.settings['done_task_prefix'] = ext_settings['done_task_prefix']
            self.settings['info_task_prefix'] = ext_settings['info_task_prefix']
            self.settings['paused_task_prefix'] = ext_settings['paused_task_prefix']
            self.settings['for_rescheduling_task_prefix'] = ext_settings['for_rescheduling_task_prefix']
            self.settings['rescheduled_periodic_task_prefix'] = ext_settings['rescheduled_periodic_task_prefix']
            self.settings['day_symbol'] = ext_settings['day_symbol']
            self.settings['month_symbol'] = ext_settings['month_symbol']
            self.settings['year_symbol'] = ext_settings['year_symbol']
            self.settings['date_separator'] = ext_settings['date_separator']
            self.settings['time_separator'] = ext_settings['time_separator']
            self.settings['log_entry_prefix'] = ext_settings['log_entry_prefix']
            self.settings['log_line_length'] = int(ext_settings['log_line_length'])
            self.settings['earned_time_balance_form'] = ext_settings['earned_time_balance_form']
            self.settings['atlas_files_extension'] = ext_settings["atlas_files_extension"]
            self.settings['get_data_from_calendars'] = ext_settings['get_data_from_calendars']
            self.settings['active_task_prefixes'] = [self.settings['open_task_prefix'], self.settings['top_task_prefix']]
            self.settings['reserved_word_prefixes'] = [self.settings['tag_prefix'], self.settings['cat_prefix']]

