--create database lsdb with owner ls;


create table products (
    product_id serial not null constraint products_pk primary key,
    name varchar(255) not null,
    price double precision default 0 not null,
    quantity integer default 0 not null,
    create_time timestamp default now() not null
);

-- alter table products owner to ls;

create unique index products_product_id_uindex on products (product_id);
create unique index products_name_uindex on products (name);
