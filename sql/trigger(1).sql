delimiter #
create trigger T1
after update on company_company
for each row
begin
    if (new.uniform_social_credit_code != old.uniform_social_credit_code) then
        insert into company_change(change_date, change_item, before_change, after_change,create_date, company_id)
        values(curdate(),"统一社会信用代码",old.uniform_social_credit_code,new.uniform_social_credit_code,curdate(),old.id);
    else if(new.name != old.name) then
        insert into company_change(change_date, change_item, before_change, after_change,create_date, company_id)
        values(curdate(),"企业名称",old.name,new.name,curdate(),old.id);
    else if(new.registered_capital != old.registered_capital) then
        insert into company_change(change_date, change_item, before_change, after_change,create_date, company_id)
        values(curdate(),"注册资本",old.registered_capital,new.registered_capital,curdate(),old.id);
    else if(new.paid_up_capital != old.paid_up_capital) then
        insert into company_change(change_date, change_item, before_change, after_change,create_date, company_id)
        values(curdate(),"实缴资本",old.paid_up_capital,new.paid_up_capital,curdate(),old.id);
    else if(new.business_scope != old.business_scope) then
        insert into company_change(change_date, change_item, before_change, after_change,create_date, company_id)
        values(curdate(),"经营范围",old.business_scope,new.business_scope,curdate(),old.id);
    else if(new.industry != old.industry) then
        insert into company_change(change_date, change_item, before_change, after_change,create_date, company_id)
        values(curdate(),"所属行业",old.industry,new.industry,curdate(),old.id);
    else if(new.tel != old.tel) then
        insert into company_change(change_date, change_item, before_change, after_change,create_date, company_id)
        values(curdate(),"电话",old.tel,new.tel,curdate(),old.id);
    else if(new.email != old.email) then
        insert into company_change(change_date, change_item, before_change, after_change,create_date, company_id)
        values(curdate(),"邮箱",old.email,new.email,curdate(),old.id);
    else if(new.province != old.province) then
        insert into company_change(change_date, change_item, before_change, after_change,create_date, company_id)
        values(curdate(),"省",old.province,new.province,curdate(),old.id);
    else if(new.city != old.city) then
        insert into company_change(change_date, change_item, before_change, after_change,create_date, company_id)
        values(curdate(),"市",old.city,new.city,curdate(),old.id);
    else if(new.district != old.district) then
        insert into company_change(change_date, change_item, before_change, after_change,create_date, company_id)
        values(curdate(),"县/区",old.district,new.district,curdate(),old.id);
    else if(new.detail_address != old.detail_address) then
        insert into company_change(change_date, change_item, before_change, after_change,create_date, company_id)
        values(curdate(),"详细地址",old.detail_address,new.detail_address,curdate(),old.id);
    else if(new.company_type != old.company_type) then
        insert into company_change(change_date, change_item, before_change, after_change,create_date, company_id)
        values(curdate(),"企业类型",old.company_type,new.company_type,curdate(),old.id);
    else if(new.business_registration_number != old.business_registration_number) then
        insert into company_change(change_date, change_item, before_change, after_change,create_date, company_id)
        values(curdate(),"工商注册号",old.business_registration_number,new.business_registration_number,curdate(),old.id);
    else if(new.registration_authority != old.registration_authority) then
        insert into company_change(change_date, change_item, before_change, after_change,create_date, company_id)
        values(curdate(),"登记机关",old.registration_authority,new.registration_authority,curdate(),old.id);
    else if(new.operating_status != old.operating_status) then
        insert into company_change(change_date, change_item, before_change, after_change,create_date, company_id)
        values(curdate(),"经营状态",old.operating_status,new.operating_status,curdate(),old.id);
    end if;
    end if;
    end if;
    end if;
    end if;
    end if;
    end if;
    end if;
    end if;
    end if;
    end if;
    end if;
    end if;
    end if;
    end if;
    end if;
end;
#
delimiter ;
