%{
-> session2.Session
---
activity: longblob    # electric activity of the neuron
%}

classdef Neuron < dj.Imported

	methods(Access=protected)

		function makeTuples(self, key)
            % use the key struct to determine the data file path
            data_file = sprintf('data/data_%d_%s', key.mouse_id, key.session_date);
            
            % load the data file
            data = load(data_file, 'data');
            
            % add the loaded data as the "activity" column
            key.activity = data.data;
            
			% insert the key into self
            self.insert(key)
		end
	end

end