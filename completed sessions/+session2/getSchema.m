function obj = getSchema
persistent schemaObject
if isempty(schemaObject)
    username = dj.conn().user;
    schemaObject = dj.Schema(dj.conn, 'session2', sprintf('%s_workshop_session2', username));
end
obj = schemaObject;
end
