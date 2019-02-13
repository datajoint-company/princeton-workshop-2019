function obj = getSchema
persistent schemaObject
if isempty(schemaObject)
    schemaObject = dj.Schema(dj.conn, 'session3', 'shan_workshop_session3');
end
obj = schemaObject;
end
