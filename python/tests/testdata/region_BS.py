"""Auto-generated file, do not edit by hand. BS metadata"""
from phonenumbers.phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BS = PhoneMetadata(id='BS', country_code=1, international_prefix='011',
    general_desc=PhoneNumberDesc(national_number_pattern='(242|8(00|66|77|88)|900)\\d{7}', possible_number_pattern='\\d{7,10}', possible_length=(10,), possible_length_local_only=(7,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='242(?:3(?:02|[236][1-9]|4[0-24-9]|5[0-68]|7[3-57]|9[2-5])|4(?:2[237]|51|64|77)|502|636|702)\\d{4}', possible_length=(10,), possible_length_local_only=(7,)),
    mobile=PhoneNumberDesc(national_number_pattern='242(357|359|457|557)\\d{4}', possible_number_pattern='\\d{10}', possible_length=(10,)),
    toll_free=PhoneNumberDesc(national_number_pattern='8(00|66|77|88)\\d{7}', possible_number_pattern='\\d{10}', possible_length=(10,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='900\\d{7}', possible_number_pattern='\\d{10}', possible_length=(10,)),
    shared_cost=PhoneNumberDesc(),
    personal_number=PhoneNumberDesc(),
    voip=PhoneNumberDesc(),
    pager=PhoneNumberDesc(),
    uan=PhoneNumberDesc(),
    voicemail=PhoneNumberDesc(),
    no_international_dialling=PhoneNumberDesc(),
    national_prefix='1',
    national_prefix_for_parsing='1')
