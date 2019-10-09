$(document).ready(function () {

    // update modal form with existing data
    $('.update-task').click(function () {
        const id = $(this).attr('id');

        $.get('tasks/get-task-json/' + id, function (data, status) {
            if (status === 'success') {

                // set form action url
                $('#update_task_form').attr('action', 'tasks/update/' + data.id);

                // set form inputs with existing data
                $('#title').val(data.title);
                $('#detail').val(data.detail);
                $('#due_date').val(data.due_date);
            }
        })

    });

    // permission alert for task deletion
    $('.delete-task').click(function () {
        const id = $(this).attr('id');
        const message = 'Sure you want to delete this task?';

        Swal.fire({
            title: 'Confirm Delete',
            text: message,
            type: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Yes, delete it!'
        }).then((result) => {
            if (result.value) {
                window.location = 'tasks/delete/' + id;
            }
        })
    });
});