function obj = getSchema
persistent schemaObject
if isempty(schemaObject)
    schemaObject = dj.Schema(dj.conn, 'subject', 'workshop_colony_subject');
end
obj = schemaObject;
end
