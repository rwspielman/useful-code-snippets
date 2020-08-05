def meta_factory(model_class, dept):
    return type('Meta', (object,),
                {'proxy': True, 'verbose_name_plural': dept, 'app_label': model_class._meta.app_label})


def proxy_model_factory(model_class, queryset_class, dept):
    Meta = meta_factory(model_class, dept.name)
    cls = type(
        dept.name,
        (model_class,),
        {
            'department': dept,
            'objects': queryset_class.as_manager(),
            '__module__': __name__,
            'Meta': Meta
        }
    )
    return cls
