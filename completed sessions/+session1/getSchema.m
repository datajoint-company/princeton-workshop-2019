function obj = getSchema
persistent schemaObject
if isempty(schemaObject)
    schemaObject = dj.Schema(dj.conn, 'session1', 'shan_workshop_session1');
end
obj = schemaObject;
end
