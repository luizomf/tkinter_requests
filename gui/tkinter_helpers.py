def grid_element(element, *args, **kwargs):
    element.grid(
        sticky=kwargs.get('sticky', 'news'),
        row=kwargs.get('row'),
        column=kwargs.get('column'),
        padx=kwargs.get('padx', 5),
        pady=kwargs.get('padx', 5),
        rowspan=kwargs.get('rowspan'),
        columnspan=kwargs.get('columnspan'),
    )
