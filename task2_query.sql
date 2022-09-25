
--How many tons worth of fruit does an average seller have?
select AVG(q.s_avg)
    from
        (select si.seller_id as s_id, SUM(si.fruit_weight) as s_avg
        from seller_info si
        group by si.seller_id) q

--How many sellers have at least one client who purchased their fruit?
select count(Distinct seller_id)
from consumption_info
where client_id IS NOT NULL and quantity_purchased_fruit IS NOT NULL --optional, as it's not clear if these values could be nulls or not        