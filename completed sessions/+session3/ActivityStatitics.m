%{
-> session3.Neuron
-----
mean: float    # mean activity
stdev: float   # standard deviation of activity
max: float     # maximum activity
%}

classdef ActivityStatitics < dj.Computed

	methods(Access=protected)

		function makeTuples(self, key)
            activity = fetch1(session2.Neuron & key, 'activity');
            
            % compute various statistics on activity
            key.mean = mean(activity);
            key.stdev = std(activity);
            key.max = max(activity);
			self.insert(key)
		end
	end

end