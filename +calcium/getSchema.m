function obj = getSchema
persistent schemaObject
if isempty(schemaObject)
    schemaObject = dj.Schema(dj.conn, 'calcium', 'workshop_2pdemo');
end
obj = schemaObject;
end
