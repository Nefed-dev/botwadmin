create table messages
(
    id           serial,
    parent_id    integer,
    button_text  varchar,
    message_text varchar,
    media        text[]
)