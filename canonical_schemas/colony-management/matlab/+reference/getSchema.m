function obj = getSchema
persistent schemaObject
if isempty(schemaObject)
    schemaObject = dj.Schema(dj.conn, 'reference', 'workshop_colony_reference');
end
obj = schemaObject;
end
