function obj = getSchema
persistent schemaObject
if isempty(schemaObject)
    schemaObject = dj.Schema(dj.conn, 'action', 'workshop_colony_action');
end
obj = schemaObject;
end
